from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.http import request

from course.models import Course


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
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=(('Male', 'Male'), ('Female', 'Female')), null=True, blank=True)
    picture = models.ImageField(upload_to='student', null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Student'

    def __str__(self):
        return self.student_user.username


class StudentCourses(models.Model):
    student = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    student_course = models.ManyToManyField(Course)

    class Meta:
        verbose_name_plural = 'Student Courses'




