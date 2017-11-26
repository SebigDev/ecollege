from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View

from course.models import *
from student.models import Student
from tutor.models import *


class IndexView(View):
    def get(self, request, *args, **kwargs):
        course = Course.objects.all().order_by('id')
        tutor = Tutor.objects.filter()
        student = Student.objects.filter()
        context = {
            'course': course,
            'tutor': tutor,
            'student': student
        }
        return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html', {})
