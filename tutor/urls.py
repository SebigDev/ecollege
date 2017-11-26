from django.conf.urls import url

from tutor.views import TutorDashboardView, TutorCourseListView, \
    TutorCourseUpdateView, TutorCourseCreateView, TutorCourseDeleteView, TutorsListView,\
    TutorProfileUpdateView, TutorProfileDetailView

urlpatterns = [
    url(r'^(?P<pk>\d+)/dashboard/$', TutorDashboardView.as_view(), name='dashboard_list'),
    url(r'^allTutors/$', TutorsListView.as_view(), name='tutors_all'),
    url(r'^(?P<pk>\d+)/courses/$', TutorCourseListView.as_view(), name='tutor_course'),
    url(r'^courses/create/$', TutorCourseCreateView.as_view(), name='tutor_create'),
    url(r'^(?P<pk>\d+)/courses/edit/$', TutorCourseUpdateView.as_view(), name='tutor_edit'),
    url(r'^(?P<pk>\d+)/courses/delete/$', TutorCourseDeleteView.as_view(), name='tutor_delete'),
    url(r'^(?P<tutor_user>\w+)/(?P<pk>\d+)/profile/$', TutorProfileDetailView.as_view(), name='profile'),
    url(r'^(?P<tutor_user>\w+)/(?P<pk>\d+)/profile/edit/$', TutorProfileUpdateView.as_view(), name='profile_edit'),

]
