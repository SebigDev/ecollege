from django.conf.urls import url
from .import views


urlpatterns = [
    url(r'^dashboard$', views.student_dashboard, name='student_dashboard'),
    url(r'^all-courses-available/$', views.all_course_list, name='all_course_list'),
    url(r'^my-courses/$', views.students_courses, name='my_courses'),
    url(r'^start-course/(?P<slug>[\w-]+)/$', views.student_take_course, name='student_take_course'),
    url(r'^register-courses/$', views.StudentCourseCreateView.as_view(), name='register_course'),
    url(r'^(?P<pk>\d+)/delete-courses/$', views.StudentCourseDeleteView.as_view(), name='delete_course'),
]
