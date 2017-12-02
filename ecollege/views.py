
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from course.models import Course
from student.models import Student
from tutor.models import Tutor


def index(request):
    if request.user.is_staff and request.user.is_authenticated():
        tutor = get_object_or_404(Tutor, tutor_user=request.user)
        course = Course.objects.all()
        return render(request, 'index.html', {'tutor': tutor, 'course': course})

    if request.user.is_active and request.user.is_authenticated():
        student = get_object_or_404(Student, student_user=request.user)
        course = Course.objects.all()

        return render(request, 'index.html', {'student': student, 'course': course})

    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html', {})


def login_redirect(request):
    if request.user.is_superuser:
        return HttpResponseRedirect('/admin')

    if request.user.is_staff and request.user.is_authenticated():
        tutor = get_object_or_404(Tutor, tutor_user=request.user)
        return HttpResponseRedirect(reverse('dashboard_list', kwargs={'pk': tutor.pk}))

    if request.user.is_active and request.user.is_authenticated():
        student = get_object_or_404(Student, student_user=request.user)
        return HttpResponseRedirect(reverse('student_dashboard', student))


def success_reg(request):
    if request.user.is_active:
        return render(request, 'success_reg.html')
    else:
        return HttpResponseRedirect('/accounts/signup',)

