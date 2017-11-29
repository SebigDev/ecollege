from django.contrib import admin
from .models import Student, StudentCourses


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_user', 'age', 'gender']
    list_filter = ['student_user', 'age', 'gender']
    search_fields = ['student_user', 'age', 'gender']


@admin.register(StudentCourses)
class StudentCoursesAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, student, request, **kwargs):
        if student.name == 'student':
            kwargs['initial'] = request.user.id
        return super(StudentCoursesAdmin, self).formfield_for_foreignkey(
            student, request, **kwargs
        )





