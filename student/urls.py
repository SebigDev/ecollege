from django.conf.urls import url

from student.views import StudentDashboardView, StudentCourseList
from .import views


urlpatterns = [
    url(r'^(?P<pk>\d+)/dashboard$', StudentDashboardView.as_view(), name='student_dashboard'),
    url(r'^course_listing/$', StudentCourseList.as_view(), name='course_available'),

]