from django.db import models
from django.urls import reverse

from tutor.models import Tutor


class CourseCategory(models.Model):
    course_type = models.CharField(max_length=200)
    course_level = models.CharField(max_length=255, choices=(('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')))

    class Meta:
        verbose_name_plural = 'Course Category'

    def __str__(self):
        return '{} {}'.format(self.course_type, self.course_level)


class Course(models.Model):
    category = models.ManyToManyField(CourseCategory, related_name='course_category')
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='course')
    blob = models.CharField(max_length=500)
    description = models.TextField()
    tutor = models.ManyToManyField(Tutor)
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Course'

    def __str__(self):
        return self.title


class Topic(models.Model):
    topics_course = models.ForeignKey(Course, blank=True)
    topic_chapter = models.PositiveIntegerField()
    topic_title = models.CharField(max_length=200)
    topic_description = models.TextField()
    topic_duration = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = 'Topic'

    def __str__(self):
        return self.topic_title
