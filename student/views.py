from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView

from course.models import Course
from student.models import Student


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





