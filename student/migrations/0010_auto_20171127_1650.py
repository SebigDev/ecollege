# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 15:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_auto_20171127_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcourse',
            name='my_course',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.Course'),
        ),
    ]