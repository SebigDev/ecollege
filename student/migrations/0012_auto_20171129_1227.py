# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 11:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_auto_20171129_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcourses',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
