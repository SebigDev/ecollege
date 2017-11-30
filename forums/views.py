from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from forums.models import Forum, ForumThread
from student.models import Student


@login_required
def forum_index(request):
    if request.user.is_active and request.user.is_authenticated():
        student = get_object_or_404(Student, student_user=request.user)
        forum = Forum.objects.filter()
        context = {
            'student': student,
            'forum': forum
        }
        return render(request, 'forum/forum.html', context)


@login_required
def forum_thread(request, forum_name):
    if request.user.is_active and request.user.is_authenticated():
        try:
            student = Student.objects.all()
        except Student.DoesNotExist:
            raise Http404
        name_forum = Forum.objects.filter(forum_name=request.user)
        forum_thread_list = ForumThread.objects.filter()

        context = {
            'student': student,
            'name_forum': name_forum,
            'forum_thread_list': forum_thread_list
        }
        return render(request, 'forum/thread.html', context)
