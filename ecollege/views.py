from django.contrib.auth.models import User
from django.forms import ModelForm
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
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
        return HttpResponseRedirect(reverse('all_course_list',))


class StudentRegForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


def student_sign_up(request):
    if request.user.is_active and request.user.is_authenticated():
        user = get_object_or_404(User, username=request.user)
        form = StudentRegForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'student_signup.html', {'user': user, 'form': form})


class TutorRegForm(ModelForm):
    class Meta:
        model = Tutor
        fields = '__all__'


def tutor_sign_up(request):
    if request.user.is_staff and request.user.is_authenticated():
        user = get_object_or_404(User, username=request.user)
        form = TutorRegForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'tutor_signup.html', {'user': user, 'form': form})


def success_reg(request):
    if request.user.is_staff and request.user.is_authenticated():
        return HttpResponseRedirect(reverse('tutor_sign_up'))

    if request.user.is_active and request.user.is_authenticated():
        return HttpResponseRedirect(reverse('student_sign_up'))

    else:
        return HttpResponseRedirect('/accounts/signup',)

