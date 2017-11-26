from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


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
    photo = models.ImageField(upload_to='tutor', null=True)
    designation = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    activation_key = models.CharField(max_length=255, default=1)
    email_validated = models.BooleanField(default=False)
    website = models.URLField()
    address = models.CharField(max_length=500)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    bio = models.TextField()

    class Meta:
        verbose_name_plural = 'Tutor'

    def __str__(self):
        return self.tutor_user.username
