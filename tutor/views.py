from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from django.urls import reverse
from django.views.generic import UpdateView, CreateView

from tutor.models import Tutor
from course.models import Course, Topic
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


class TutorCourseUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'tutor/edit.html'
    model = Course
    fields = ['title', 'slug', 'image', 'blob', 'description', 'tutor']

    def get_context_data(self, **kwargs):
        context = super(TutorCourseUpdateView, self).get_context_data(**kwargs)
        context['course'] = Course.objects.filter(category=self.object.pk)
        context['tutor'] = get_object_or_404(Tutor, tutor_user=self.request.user)
        context['topic'] = Topic.objects.filter(topics_course=self.object)
        return context

    def form_valid(self, form):
            form.instance.course = self.request.user
            return super(TutorCourseUpdateView, self).form_valid(form)

    def get_success_url(self):
            return reverse('tutor_course', kwargs={'pk': self.object.pk})


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


@login_required
def tutor_profile(request, pk, tutor_user):
    if request.user.is_authenticated:
        tutor = get_object_or_404(Tutor, tutor_user=request.user)
        return render(request, 'tutor/profile.html', {'tutor': tutor})


@login_required
def tutor_update(request, pk, tutor_user):
    tutor = get_object_or_404(Tutor, pk=pk, tutor_user=request.user)
    form = TutorDataForm(request.POST or None, instance=tutor)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('profile', tutor_user, pk)
    return render(request, 'tutor/edit.html', {'form': form, 'tutor': tutor})


@login_required
def tutor_student_list(request, pk):
    tutor = get_object_or_404(Tutor, pk=pk, tutor_user=request.user)
    list_student = Student.objects.all().order_by('id')
    return render(request, 'tutor/student_list.html', {'list_student': list_student, 'tutor': tutor})


def tutor_course_topics(request, pk, topic_title):
    if request.user.is_staff and request.user.is_authenticated():
        course = Course.objects.get(tutor__tutor_user=request.user, pk=pk)
        tutor = get_object_or_404(Tutor, tutor_user=request.user)
        topic = Topic.objects.filter(topics_course=pk).order_by('id')
        return render(request, 'tutor/topic_course.html', {'course': course, 'topic': topic, 'tutor': tutor})


class TutorCreateTopicView(LoginRequiredMixin, CreateView):
    model = Topic
    template_name = 'tutor/topic.html'
    fields = ['topics_course', 'topic_chapter', 'topic_title', 'topic_description', 'topic_duration']

    def get_context_data(self, **kwargs):
        context = super(TutorCreateTopicView, self).get_context_data(**kwargs)
        context['tutor'] = get_object_or_404(Tutor, tutor_user=self.request.user)
        return context

    def form_valid(self, form):
            form.fields.topics_course = self.object
            return super(TutorCreateTopicView, self).form_valid(form)

    def get_success_url(self):
            return reverse('tutor_course_topics', kwargs={
                'pk': self.object.pk, 'slug': self.object.slug
            })


class TutorTopicUpdateView(LoginRequiredMixin, UpdateView):
    model = Topic
    fields = ['topic_chapter', 'topic_title', 'topic_description', 'topic_duration']
    template_name = 'tutor/topic_form.html'

    def get_context_data(self, **kwargs):
        context = super(TutorTopicUpdateView, self).get_context_data(**kwargs)
        context['tutor'] = get_object_or_404(Tutor, tutor_user=self.request.user)
        return context

    def get_success_url(self):
        return reverse('tutor_course_topics', kwargs={
                'pk': self.object.pk
            })







