# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 11:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_student_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentcourse',
            name='_student',
        ),
        migrations.DeleteModel(
            name='StudentCourse',
        ),
    ]
