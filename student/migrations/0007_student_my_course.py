# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_auto_20171117_1000'),
        ('student', '0006_student_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='my_course',
            field=models.ManyToManyField(to='course.Course'),
        ),
    ]
