# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 11:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20171119_0337'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Student'), (2, 'Tutor'), (3, 'Admin')], null=True),
        ),
    ]
