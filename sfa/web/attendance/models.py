from django.db import models


class Teacher(models.Model):
    user = models.OneToOneField('auth.User', related_name="teacher", on_delete=models.CASCADE)
    id_number = models.IntegerField()
    phone_number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "Teacher {}".format(self.user.get_full_name())


class YearLevel(models.Model):
    level = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.level)


class Section(models.Model):
    name = models.CharField(max_length=100)
    teachers = models.ManyToManyField('attendance.Teacher', related_name="sections")
    level = models.ForeignKey('attendance.YearLevel', related_name="sections", on_delete=models.CASCADE)
    
    def __str__(self):
        return "{} {}".format(self.name, self.level)


class Student(models.Model):
    student_number = models.CharField(max_length = 100, unique=True)
    section = models.ForeignKey('attendance.Section', related_name="students", on_delete=models.CASCADE)    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class StudentGuardian(models.Model):
    students = models.ManyToManyField('attendance.Student', related_name="guardians")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.IntegerField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


ATTENDANCE_STATUS = (
    ('---------','Select one'),
    ('present', 'Present'),
    ('absent', 'Absent'),
    ('exempted', 'Exempted')
)

class Attendance(models.Model):
    student = models.ForeignKey('attendance.Student', related_name="attendance", on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=ATTENDANCE_STATUS)
    date = models.DateTimeField(auto_now_add=True)