from django.conf.urls import url

from tutor.views import TutorDashboardView, TutorCourseListView, \
    TutorCourseUpdateView, TutorCourseCreateView, TutorCourseDeleteView


urlpatterns = [
    url(r'^dashboard/$', TutorDashboardView.as_view(), name='dashboard_list'),
    url(r'^(?P<first_name>\w+)/courses/$', TutorCourseListView.as_view(), name='tutor_course'),
    url(r'^(?P<pk>\d+)/courses/delete/$', TutorCourseDeleteView.as_view(), name='tutor_delete'),
    url(r'^(?P<first_name>\w+)/courses/create/$', TutorCourseCreateView.as_view(), name='tutor_create'),
    url(r'^myCourses/(?P<pk>\d+)/edit/$', TutorCourseUpdateView.as_view(), name='tutor_edit'),
    #url(r'^profile/(?P<pk>\d+)/$', views.profile, name='profile'),

]
