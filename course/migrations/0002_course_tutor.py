# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='tutor',
            field=models.ManyToManyField(null=True, to='tutor.Tutor'),
        ),
    ]
