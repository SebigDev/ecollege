from django.contrib import admin
from .models import Tutor, TutorStudent


@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ['tutor_user', 'designation', 'phone', 'website']
    list_filter = ['designation']
    search_fields = ['designation']


@admin.register(TutorStudent)
class TutorStudentAdmin(admin.ModelAdmin):
    list_display = ['pk']
    list_filter = ['tutor_student']
    search_fields = ['tutor_student']
