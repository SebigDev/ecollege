from django.conf.urls import url

from student.views import StudentDashboardView, StudentCourseList, StudentProfileDetailView, \
    StudentProfileUpdateView, StudentSelectCourseCreateView, StudentRegisteredCoursesView
from .import views


urlpatterns = [
    url(r'^(?P<pk>\d+)/dashboard$', StudentDashboardView.as_view(), name='student_dashboard'),
    url(r'^course_listing/$', StudentCourseList.as_view(), name='course_available'),
    url(r'^(?P<pk>\d+)/profile/$', StudentProfileDetailView.as_view(), name='student_profile'),
    url(r'^(?P<pk>\d+)/profile/edit/$', StudentProfileUpdateView.as_view(), name='profile_edit'),
    url(r'^(?P<pk>\d+)/profile/select-courses/$', StudentSelectCourseCreateView.as_view(), name='student_course'),
    url(r'^(?P<pk>\d+)/profile/my-courses/$', StudentRegisteredCoursesView.as_view(), name='my_courses'),
]
