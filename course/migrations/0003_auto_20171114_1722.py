# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_tutor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='tutor',
            field=models.ManyToManyField(to='tutor.Tutor'),
        ),
    ]
