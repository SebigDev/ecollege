# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_auto_20171115_0900'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
