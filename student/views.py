from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelForm
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import CreateView

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
def student_take_course(request, pk, slug):
    if request.user.is_active and request.user.is_authenticated():
        student = Student.objects.get(student_user=request.user)
        topic = Topic.objects.filter(topics_course=pk).order_by('id')
        course = get_object_or_404(Course, pk=pk)
        return render(request, 'student/enrolled_course.html', {
            'topic': topic, 'course': course, 'student': student
        })


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['address', 'state', 'country']


@login_required
def student_profile(request):
    if request.user.is_active and request.user.is_authenticated():
        student = get_object_or_404(Student, student_user=request.user)
        return render(request, 'student/profile.html', {'student': student})


@login_required
def profile_update(request, pk):
    student = get_object_or_404(Student, pk=pk, student_user=request.user)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_profile')
    return render(request, 'student/update_profile.html', {'form': form, 'student': student})


class StudentCourseCreateView(LoginRequiredMixin, CreateView):
    template_name = 'student/student_form.html'
    model = StudentCourses
    fields = ['student', 'student_course']

    def get_context_data(self, **kwargs):
        context = super(StudentCourseCreateView, self).get_context_data(**kwargs)
        context['student'] = get_object_or_404(Student, student_user=self.request.user,)
        context['student_course'] = StudentCourses.objects.filter(pk=self.object)
        return context

    def get_success_url(self):
        return reverse('my_courses', )


