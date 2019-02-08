from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.conf import settings
from account.utils import default_redirect
from account.compat import is_authenticated
from django.utils import timezone
from django.contrib import messages

from school.helpers import send_sms
from .models import *
from .forms import *


class HomePageView(generic.TemplateView):
    template_name = "homepage.html"
    redirect_field_name = "next"

    def get(self, *args, **kwargs):
        if is_authenticated(self.request.user):
            return redirect(self.get_success_url())
        return super().get(*args, **kwargs)
    
    def get_success_url(self, fallback_url=None, **kwargs):
        if fallback_url is None:
            fallback_url = settings.ACCOUNT_LOGIN_REDIRECT_URL
        kwargs.setdefault("redirect_field_name", self.get_redirect_field_name())
        return default_redirect(self.request, fallback_url, **kwargs)

    def get_redirect_field_name(self):
        return self.redirect_field_name


class AttendanceHome(LoginRequiredMixin, generic.TemplateView):
    template_name = 'attendance/home.html'


class SectionListView(LoginRequiredMixin, generic.ListView):
    template_name = 'attendance/section.html'
    model = Section
    context_object_name = "sections"

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        qs = qs.filter(teachers__user__in=[user])
        return qs


class SectionStudentList(LoginRequiredMixin, generic.FormView):
    template_name = 'attendance/student_list.html'
    section = None
    form_class = AttendanceForm
    success_url = reverse_lazy('attendance:sections')

    def dispatch(self, request, *args, **kwargs):
        self.get_section()
        return super().dispatch(request, *args, **kwargs)

    def get_section(self):
        sec_id = self.kwargs.get('section_id', 0)
        self.section = get_object_or_404(Section, pk=sec_id)
        return self.section

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = self.section
        context['post_url'] = reverse_lazy('attendance:stud_list', kwargs={"section_id": self.section.id })
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['section'] = self.section
        return kwargs

    def form_valid(self, form):
        data = form.cleaned_data
        for student in self.section.students.all():
            attendance_obj, is_created = Attendance.objects.get_or_create(
                student = student,
                status ='absent',
                date = timezone.now()
            )
            if student in data['ordersSelect']:
                attendance_obj.status = 'present'
                attendance_obj.save()
            else:
                for guardian in student.guardians.all():
                    if guardian.phone_number:
                        txt_details = {
                            'message': "Dear {}, This is to inform you that your child is absent during this time '{}'. 'SFA'".format(student.last_name, timezone.now()),
                            'number': '+{}'.format(guardian.phone_number)
                        }

                        send_sms(txt_details)


        messages.success(self.request, "Attendance has been submitted and parents is notified.")

        return super().form_valid(form)

    

