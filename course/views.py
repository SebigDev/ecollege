from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from .models import *


class CourseListView(LoginRequiredMixin, ListView):
    template_name = 'course/list.html'
    model = Course
    context_object_name = 'course_listing'
    login_url = '/account/login'
    redirect_field_name = 'redirect_to'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(CourseListView, self).get_context_data(**kwargs)
        context['tutor'] = Tutor.objects.get(tutor_user=self.request.user)
        context['course'] = Course.objects.filter(tutor__tutor_user=self.request.user)
        return context


class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    context_object_name = 'course_detail'
    template_name = 'course/detail.html'
    login_url = '/account/login'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['tutor'] = Tutor.objects.get(tutor_user=self.request.user)
        context['course'] = Course.objects.filter(tutor__tutor_user=self.request.user)
        return context


class CourseEnrolDetailView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'course/enrol.html'
    context_object_name = 'course_enrol'
    login_url = '/account/login'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super(CourseEnrolDetailView, self).get_context_data(**kwargs)
        context['topic'] = Topic.objects.filter(topics_course=self.object).order_by('id')
        context['tutor'] = Tutor.objects.get(tutor_user=self.request.user)
        context['course_cat'] = CourseCategory.objects.filter(course_category=self.object)
        return context







