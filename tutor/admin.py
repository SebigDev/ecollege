from django.contrib import admin
from .models import Tutor


@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ['tutor_user', 'designation', 'phone', 'website']
    list_filter = ['designation']
    search_fields = ['designation']

