from django.conf import settings

from django.conf.urls.static import static
from django.urls import include, path
from django.views.generic import TemplateView

from django.contrib import admin
from attendance.views import *

app_name = "attendance"

urlpatterns = [
    path("home/", AttendanceHome.as_view(), name="home"),
    path("sections/", SectionListView.as_view(), name="sections"),
    path("student/list/<int:section_id>", SectionStudentList.as_view(), name="stud_list"),

]

