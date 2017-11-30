from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import CreateView, DeleteView

from course.models import Course, Topic, CourseCategory
from student.models import Student, StudentCourses


@login_required
def student_dashboard(request):
    if request.user.is_active and request.user.is_authenticated():
        student = get_object_or_404(Student, student_user=request.user)
        course = Course.objects.all().filter(studentcourses__student=request.user)
        context = {
            'student': student,
            'course': course
        }
        return render(request, 'student/student_dashboard.html', context)


@login_required
def all_course_list(request):
    if request.user.is_active and request.user.is_authenticated():
        try:
            course = Course.objects.all()
        except Course.DoesNotExist:
            raise Http404
        student = get_object_or_404(Student, student_user=request.user)
        context = {'course': course, 'student': student}
        return render(request, 'student/course_list.html', context)


@login_required
def students_courses(request):
    if request.user.is_active and request.user.is_authenticated():
        student = get_object_or_404(Student, student_user=request.user)
        course = Course.objects.all().filter(studentcourses__student=request.user)
        return render(request, 'student/all_courses.html', {
            'student': student,
            'course': course
        })


@login_required
def student_take_course(request, slug):
    if request.user.is_active and request.user.is_authenticated():
        student = Student.objects.get(student_user=request.user)
        topic = Topic.objects.filter(topics_course__studentcourses__student=request.user).order_by('id')
        course = Course.objects.get(studentcourses__student_id=request.user)
        return render(request, 'student/enrolled_course.html', {
            'topic': topic, 'course': course, 'student': student
        })


@login_required
def student_profile(request):
    if request.user.is_active:
        student = get_object_or_404(Student, student_user=request.user)
        return render(request, 'student/profile.html', {'student': student})


class StudentCourseCreateView(LoginRequiredMixin, CreateView):
    template_name = 'student/student_form.html'
    model = StudentCourses
    fields = ['student', 'student_course']

    def get_context_data(self, **kwargs):
        context = super(StudentCourseCreateView, self).get_context_data(**kwargs)
        try:
            context['student'] = Student.objects.get(student_user=self.request.user)
        except Student.DoesNotExist:
            raise Http404
        return context

    def get_success_url(self):
        return reverse('my_courses', )


