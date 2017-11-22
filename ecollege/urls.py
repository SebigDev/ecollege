from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from .import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^account/', include('account.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^student/', include('student.urls')),
    url(r'^course/', include('course.urls')),
    url(r'^tutor/', include('tutor.urls')),
    url(r'^contact$', views.contact, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
