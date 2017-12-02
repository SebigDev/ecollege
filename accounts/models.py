from django.contrib.auth.models import User
from accounts.forms import forms
from student.models import Student
from tutor.models import Tutor


class UserForm(forms.ModelForm):
        class Meta:
                model = User
                fields = ["username", "first_name", "last_name", "email", "is_staff", "is_active", "password"]

