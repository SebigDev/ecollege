from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from tutor.models import Tutor
from course.models import Course


class TutorDashboardView(LoginRequiredMixin, ListView):
    model = Tutor
    context_object_name = 'dashboard_list'
    template_name = 'tutor/tutor_board.html'
    login_url = '/account/login'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super(TutorDashboardView, self).get_context_data(**kwargs)
        context['tutor'] = Tutor.objects.filter(tutor_user=self.request.user)
        context['course'] = Course.objects.filter(tutor__tutor_user=self.request.user)
        return context


class TutorCourseListView(LoginRequiredMixin, ListView):
    model = Tutor
    template_name = 'tutor/tutor_course.html'
    login_url = '/account/login'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        t = super(TutorCourseListView, self).get_context_data(**kwargs)
        t['course'] = Course.objects.filter(tutor__tutor_user=self.request.user)
        return t


class TutorCourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    fields = ['category', 'title', 'slug', 'image', 'blob', 'description', 'tutor']
    template_name = 'tutor/create.html'
    success_url = reverse_lazy('tutor_course')
    login_url = '/account/login'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        return super(TutorCourseCreateView, self).form_valid(form)


class TutorCourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    fields = ['category', 'title', 'slug', 'image', 'blob', 'description', 'tutor']
    template_name = 'tutor/edit.html'
    success_url = reverse_lazy('dashboard_list')
    login_url = '/account/login'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        return super(TutorCourseUpdateView, self).form_valid(form)


class TutorCourseDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'tutor/course_list.html'
    context_object_name = 'tutor_list'
    model = Course
    login_url = 'account/login'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super(TutorCourseDeleteView, self).get_context_data(**kwargs)
        context['course'] = Course.objects.filter(tutor__tutor_user=self.request.user)
        return context






