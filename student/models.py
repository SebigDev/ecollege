from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    STUDENT = 1
    TUTOR = 2
    ADMIN = 3
    ROLE_CHOICES = (
        (STUDENT, 'Student'),
        (TUTOR, 'Tutor'),
        (ADMIN, 'Admin'),
    )
    student_user = models.OneToOneField(User, related_name='student')
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=20, choices=(('Male', 'Male'), ('Female', 'Female')))
    address = models.CharField(max_length=500)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Student'

    def __str__(self):
        return self.student_user.username


class StudentCourse(models.Model):
    _student = models.ForeignKey(Student, verbose_name='Student Assigned')

    class Meta:
        verbose_name_plural = 'Student Course'

    def __str__(self):
        return self.pk

