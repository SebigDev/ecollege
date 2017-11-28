from django.contrib import admin
from .models import Student, StudentCourse


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_user', 'age', 'gender']
    list_filter = ['student_user', 'age', 'gender']
    search_fields = ['student_user', 'age', 'gender']


@admin.register(StudentCourse)
class StudentCourseAdmin(admin.ModelAdmin):
    list_display = ['pk']




