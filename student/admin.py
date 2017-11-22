from django.contrib import admin
from .models import Student, StudentCourse


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['age', 'gender']
    list_filter = ['age', 'gender']
    search_fields = ['age', 'gender']


@admin.register(StudentCourse)
class StudentCourseAdmin(admin.ModelAdmin):
    list_display = ['pk']
    list_filter = ['_student']
    search_fields = ['_student']


