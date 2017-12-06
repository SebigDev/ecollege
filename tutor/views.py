from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from tutor.models import Tutor
from course.models import Course
from student.models import StudentCourses, Student


class TutorCourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['category', 'title', 'slug', 'image', 'blob', 'description', 'tutor']


@login_required
def tutor_dashboard(request, pk):
    tutor = get_object_or_404(Tutor, tutor_user=request.user)
    course = Course.objects.filter(tutor__tutor_user=request.user)
    student = StudentCourses.objects.filter(student__tutor__course=True)
    context = {'tutor': tutor, 'course': course, 'student': student}
    return render(request, 'tutor/tutor_board.html', context)


@login_required
def tutor_course_list(request, pk):
    tutor = get_object_or_404(Tutor, tutor_user=request.user)
    course = Course.objects.filter(tutor__tutor_user=request.user)
    context = {'tutor': tutor, 'course': course}
    return render(request, 'tutor/tutor_course.html', context)


@login_required
def tutor_create_course(request):
    tutor = get_object_or_404(Tutor, tutor_user=request.user)
    form = TutorCourseForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('tutor_course',)
    return render(request, 'tutor/create.html', {'form': form, 'tutor': tutor})


@login_required
def tutor_update_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    tutor = get_object_or_404(Tutor, tutor_user=request.user)
    form = TutorCourseForm(request.POST or None, request.FILES, instance=course,)
    if form.is_valid():
        form.save()
        return redirect('tutor_course', pk)
    return render(request, 'tutor/edit.html', {'form': form, 'course': course, 'tutor': tutor})


@login_required
def tutor_delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    tutor = get_object_or_404(Tutor, tutor_user=request.user)
    form = TutorCourseForm(request.POST or None, instance=course)
    if request.method == 'POST':
        course.delete()
        return redirect('tutor_course', pk)
    return render(request, 'tutor/tutor_confirm_delete.html', {'form': form, 'course': course, 'tutor': tutor})


@login_required
def tutor_list(request):
    our_list = Tutor.objects.all()
    log_tutor = get_object_or_404(Tutor, tutor_user=request.user)
    context = {
        'our_list': our_list,
        'log_tutor': log_tutor
    }
    return render(request, 'tutor/tutor_list.html', context)


class TutorDataForm(ModelForm):
    class Meta:
        model = Tutor
        fields = ['phone', 'website', 'bio', 'address', 'state', 'country']


def tutor_profile(request, pk, tutor_user):
    if request.user.is_authenticated:
        tutor = get_object_or_404(Tutor, tutor_user=request.user)
        return render(request, 'tutor/profile.html', {'tutor': tutor})


def tutor_update(request, pk, tutor_user):
    tutor = get_object_or_404(Tutor, pk=pk, tutor_user=request.user)
    form = TutorDataForm(request.POST or None, instance=tutor)
    if form.is_valid():
        form.save()
        return redirect('profile', tutor_user, pk)
    return render(request, 'tutor/edit.html', {'form': form, 'tutor': tutor})


@login_required
def tutor_student_list(request, pk):
    tutor = get_object_or_404(Tutor, pk=pk, tutor_user=request.user)
    list_student = Student.objects.all().order_by('id')
    return render(request, 'tutor/student_list.html', {'list_student': list_student, 'tutor': tutor})








