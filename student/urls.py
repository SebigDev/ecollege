from django.conf.urls import url
from .import views


urlpatterns = [
    url(r'^studentDashboard', views.student_dashboard, name='student_dashboard')
]