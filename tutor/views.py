from builtins import super

from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import Textarea
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from tutor.models import Tutor
from course.models import Course, CourseCategory
from student.models import StudentCourses


class TutorDashboardView(LoginRequiredMixin, DetailView):
    model = Tutor
    context_object_name = 'dashboard_list'
    template_name = 'tutor/tutor_board.html'
    login_url = '/account/login'
    redirect_field_name = 'redirect_to'
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super(TutorDashboardView, self).get_context_data(**kwargs)
        context['tutor'] = get_object_or_404(Tutor, tutor_user=self.request.user)
        context['course'] = Course.objects.filter(tutor__tutor_user=self.request.user)
        context['student'] = StudentCourses.objects.filter(student__tutor__course=True)
        return context


class TutorCourseListView(LoginRequiredMixin, DetailView):
    model = CourseCategory
    template_name = 'tutor/tutor_course.html'
    login_url = '/accounts/login'
    redirect_field_name = 'redirect_to'
    raise_exception = True

    def get_context_data(self, **kwargs):
        t = super(TutorCourseListView, self).get_context_data(**kwargs)
        t['tutor'] = get_object_or_404(Tutor, tutor_user=self.request.user)
        t['course'] = Course.objects.filter(tutor__tutor_user=self.request.user)
        return t


class TutorCourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    fields = ['category', 'title', 'slug', 'image', 'blob', 'description', 'tutor']
    template_name = 'tutor/create.html'
    redirect_field_name = 'redirect_to'
    login_url = 'account/login'

    def get_success_url(self):
        return reverse('tutor_course', kwargs={
            'pk': self.object.pk,
        })

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tutor'] = get_object_or_404(Tutor, tutor_user=self.request.user)
        return context


class TutorCourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    fields = ['category', 'title', 'slug', 'image', 'blob', 'description']
    template_name = 'tutor/edit.html'
    login_url = '/accounts/login'
    redirect_field_name = 'redirect_to'

    def get_success_url(self):
        return reverse('tutor_course', kwargs={
            'pk': self.object.pk,
        })

    def get_context_data(self, **kwargs):
        context = super(TutorCourseUpdateView, self).get_context_data(**kwargs)
        context['tutor'] = get_object_or_404(Tutor, tutor_user=self.request.user)
        return context

    def form_valid(self, form):
        return super(TutorCourseUpdateView, self).form_valid(form)


class TutorCourseDeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    login_url = '/accounts/login'
    redirect_field_name = 'redirect_to'

    def get_success_url(self):
        return reverse('tutor_course', kwargs={
            'pk': self.object.pk,
        })

    def get_context_data(self, **kwargs):
        context = super(TutorCourseDeleteView, self).get_context_data(**kwargs)
        context['tutor'] = get_object_or_404(Tutor, tutor_user=self.request.user)
        return context


class TutorsListView(LoginRequiredMixin, ListView):
    model = Tutor
    template_name = 'tutor/tutor_list.html'

    def get_context_data(self, **kwargs):
        tuts = super(TutorsListView, self).get_context_data(**kwargs)
        tuts['our_list'] = Tutor.objects.all()
        tuts['log_tutor'] = get_object_or_404(Tutor, tutor_user=self.request.user)
        return tuts


class TutorProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Tutor
    fields = ['phone', 'website', 'bio', 'address', 'state', 'country']

    def get_success_url(self):
        return reverse('profile', kwargs={
            'pk': self.object.pk,
            'tutor_user': self.object.tutor_user
        })


class TutorProfileDetailView(LoginRequiredMixin, DetailView):
    model = Tutor
    context_object_name = 'profile'
    template_name = 'tutor/profile.html'

    def get_context_data(self, **kwargs):
        context = super(TutorProfileDetailView, self).get_context_data(**kwargs)
        context['tutor'] = get_object_or_404(Tutor, tutor_user=self.request.user)
        return context










