from django.conf.urls import url

from course.views import CourseListView, CourseDetailView
from .import views


urlpatterns = [
    url(r'^all-courses/$', CourseListView.as_view(), name='course_listing'),
    url(r'^detail/(?P<pk>\w+)/(?P<slug>[\w-]+)/$', CourseDetailView.as_view(), name='course_detail'),
    url(r'^enrol/(?P<pk>\w+)/(?P<slug>[\w-]+)/$', views.CourseEnrolDetailView.as_view(), name='course_enrol')
]