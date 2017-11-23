from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View

from course.models import *
from tutor.models import *


class IndexView(View):
    def get(self, request, *args, **kwargs):
        course = Course.objects.all().order_by('id')
        tutor = Tutor.objects.filter()
        context = {
            'course': course,
            'tutor': tutor
        }
        return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html', {})
