# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0002_auto_20171130_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='forum_description',
            field=models.CharField(max_length=1000),
        ),
    ]
