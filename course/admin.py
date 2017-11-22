from django.contrib import admin
from .models import CourseCategory, Course, Topic


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ['course_type', 'course_level']
    list_filter = ['course_type', 'course_level']
    search_fields = ['course_type', 'course_level']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
    list_filter = ['title', 'created']
    search_fields = ['title', 'created']


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['topic_title', 'topic_duration']
    list_filter = ['topic_title', 'topic_duration']
    search_fields = ['topic_title']
