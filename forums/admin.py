from django.contrib import admin

from forums.models import Forum, ForumThread


@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    list_display = ['forum_name', 'forum_description']
    list_filter = ['forum_name', 'forum_description']
    search_fields = ['forum_name', 'forum_description']


@admin.register(ForumThread)
class ForumThreadAdmin(admin.ModelAdmin):
    list_display = ['forum_post', 'created']
    list_filter = ['forum_post', 'created']
    search_fields = ['forum_post', 'created']

