from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from .import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^students/', include('student.urls')),
    url(r'^forums/', include('forums.urls')),
    url(r'^courses/', include('course.urls')),
    url(r'^tutors/', include('tutor.urls')),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^success-registration/$', views.success_reg, name='success_reg'),
    url(r'^login_redirect/$', views.login_redirect, name='login_redirect'),
    url(r'^students-update/$', views.student_sign_up, name='student_sign_up'),
    url(r'^tutors-update/$', views.tutor_sign_up, name='tutor_sign_up'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
