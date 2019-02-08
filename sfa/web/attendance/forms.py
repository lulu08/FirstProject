from django import forms
from .models import Student

class AttendanceForm(forms.Form):
    ordersSelect = forms.ModelMultipleChoiceField(
        queryset = Student.objects.all(), # not optional, use .all() if unsure
        widget  = forms.CheckboxSelectMultiple,
        required = False
    )

    def __init__(self, *args, **kwargs):
        self.section = kwargs.pop('section', None)
        super().__init__(*args, **kwargs)

        if self.section:
            self.fields['ordersSelect'].queryset = self.section.students.all()
        
        # self.fields['ordersSelect'].widget = forms.HiddenInput()