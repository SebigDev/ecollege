from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView, UpdateView, CreateView

from course.models import Course
from student.models import Student, StudentCourse


class StudentDashboardView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'student/student_dashboard.html'
    login_url = 'account/login'

    def get_context_data(self, **kwargs):
        context = super(StudentDashboardView, self).get_context_data(**kwargs)
        context['student'] = Student.objects.get(student_user=self.request.user)
        return context


class StudentCourseList(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'student/course_list.html'

    def get_context_data(self, **kwargs):
        context = super(StudentCourseList, self).get_context_data(**kwargs)
        context['student'] = Student.objects.get(student_user=self.request.user)
        context['course'] = Course.objects.all()
        return context


class StudentProfileDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'student/profile.html'


class StudentProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    fields = ['address', 'state', 'country']

    def get_success_url(self):
        return reverse('student_profile', kwargs={
            'pk': self.object.pk
        })


class StudentSelectCourseCreateView(LoginRequiredMixin, CreateView):
    model = StudentCourse
    template_name = 'student/student_course.html'
    fields = ['my_course']

    def get_context_data(self, **kwargs):
        context = super(StudentSelectCourseCreateView, self).get_context_data(**kwargs)
        context['student_course'] = StudentCourse.objects.all()
        context['student'] = Student.objects.get(student_user=self.request.user)
        return context

    def get_success_url(self):
        return reverse('my_courses', kwargs={
            'pk': self.object.pk
        })


class StudentRegisteredCoursesView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'student/all_courses.html'

    def get_context_data(self, **kwargs):
        context = super(StudentRegisteredCoursesView, self).get_context_data(**kwargs)
        context['student'] = Student.objects.get(student_user=self.request.user)
        context['student_course'] = StudentCourse.objects.all()
        context['courses'] = Course.objects.filter()
        return context
