from django.conf.urls import url

from .import views


urlpatterns = [
    url(r'^forum/$', views.forum_index, name='forum_index'),
    url(r'^forum-threads/(?P<pk>\d+)/(?P<forum_name>[\w-]+)$', views.forum_thread, name='forum_thread'),
]
