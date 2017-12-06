from django.contrib.auth.models import User
from django.db import models


class Tutor(models.Model):
    STUDENT = 1
    TUTOR = 2
    ADMIN = 3
    ROLE_CHOICES = (
        (STUDENT, 'Student'),
        (TUTOR, 'Tutor'),
        (ADMIN, 'Admin'),
    )
    tutor_user = models.OneToOneField(User, related_name='tutor')
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)
    photo = models.ImageField(upload_to='tutor', null=True, blank=True)
    designation = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Tutor'

    def __str__(self):
        return self.tutor_user.username
