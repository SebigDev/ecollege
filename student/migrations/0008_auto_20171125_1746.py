# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_auto_20171117_1000'),
        ('student', '0007_student_my_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_course', models.ManyToManyField(to='course.Course')),
            ],
            options={
                'verbose_name_plural': 'Student Course',
            },
        ),
        migrations.RemoveField(
            model_name='student',
            name='my_course',
        ),
    ]
