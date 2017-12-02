from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from forums.models import Forum, ForumThread
from student.models import Student
from tutor.models import Tutor


@login_required
def forum_index(request):
    if request.user.is_staff and request.user.is_authenticated():
        tutor = get_object_or_404(Tutor, tutor_user=request.user)
        forum = Forum.objects.filter()
        user = User.objects.all()
        context = {
            'tutor': tutor,
            'forum': forum,
            'user': user
        }
        return render(request, 'forum/forum.html', context)

    if request.user.is_active and request.user.is_authenticated():
        student = get_object_or_404(Student, student_user=request.user)
        forum = Forum.objects.filter()
        user = User.objects.all()
        context = {
            'student': student,
            'forum': forum,
            'user': user
        }
        return render(request, 'forum/forum.html', context)


@login_required
def forum_thread(request, pk, forum_name):
    if request.user.is_staff and request.user.is_authenticated():
        tutor = Tutor.objects.get(tutor_user=request.user)
        name_forum = Forum.objects.get(forumthread=pk)
        forum_thread_list = ForumThread.objects.filter()
        user = User.objects.filter()

        context = {
            'name_forum': name_forum,
            'forum_thread_list': forum_thread_list,
            'user': user,
            'tutor': tutor
        }
        return render(request, 'forum/thread.html', context)

    if request.user.is_active and request.user.is_authenticated():
        student = Student.objects.get(student_user=request.user)
        name_forum = Forum.objects.get(forumthread=pk)
        forum_thread_list = ForumThread.objects.filter()
        user = User.objects.filter()

        context = {
            'student': student,
            'name_forum': name_forum,
            'forum_thread_list': forum_thread_list,
            'user': user,
        }
        return render(request, 'forum/thread.html', context)

