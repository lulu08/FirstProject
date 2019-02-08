from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *


class TeacherAdmin(ImportExportModelAdmin):
    search_fields = ['user__first_name', 'user__last_name', 'id_number']
    list_display = ['user', 'id_number']


class YearLevelAdmin(ImportExportModelAdmin):
    list_display = ['level']


class SectionAdmin(ImportExportModelAdmin):
    list_display = ['name', 'level']


class StudentAdmin(ImportExportModelAdmin):
    search_fields = ['section', 'first_name', 'last_name']
    list_display = ['student_number', 'section', 'first_name', 'last_name', 'email']
    

class StudentGuardianAdmin(ImportExportModelAdmin):
    list_display = ['first_name', 'last_name', 'email']


class AttendanceAdmin(ImportExportModelAdmin):
    list_display = ['student', 'status', 'date']



admin.site.register(Teacher, TeacherAdmin)
admin.site.register(YearLevel, YearLevelAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(StudentGuardian, StudentGuardianAdmin)
admin.site.register(Attendance, AttendanceAdmin)




