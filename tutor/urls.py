from django.conf.urls import url
from .import views


urlpatterns = [
    url(r'^(?P<pk>\d+)/dashboard/$', views.tutor_dashboard, name='dashboard_list'),
    url(r'^(?P<pk>\d+)/student-list/$', views.tutor_student_list, name='tutor_student_list'),
    url(r'^all-tutors/$', views.tutor_list, name='tutors_all'),
    url(r'^(?P<pk>\d+)/courses/$', views.tutor_course_list, name='tutor_course'),
    url(r'^courses/create-courses/$', views.tutor_create_course, name='tutor_create'),
    url(r'^(?P<pk>\d+)/courses/(?P<slug>[\w-]+)/edit-course/$',
        views.TutorCourseUpdateView.as_view(), name='tutor_edit'),
    url(r'^(?P<pk>\d+)/(?P<slug>[\w-]+)/add-topic/$', views.TutorCreateTopicView.as_view(),  name='tutor_create_topic'),
    url(r'^(?P<pk>\d+)/topic/$', views.tutor_course_topics,  name='tutor_course_topics'),
    url(r'^(?P<pk>\d+)/(?P<topic_title>[\w-]+)/topic/update$',
        views.TutorTopicUpdateView.as_view(),  name='topic_update'),
    url(r'^(?P<pk>\d+)/courses/delete-course/$', views.tutor_delete_course, name='tutor_delete'),
    url(r'^(?P<tutor_user>\w+)/(?P<pk>\d+)/profile$', views.tutor_profile, name='profile'),
    url(r'^(?P<tutor_user>\w+)/(?P<pk>\d+)/profile/edit-profile/$', views.tutor_update, name='profile_edit'),
]
