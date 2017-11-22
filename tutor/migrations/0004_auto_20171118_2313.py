# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-18 22:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tutor', '0003_auto_20171116_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutor',
            name='email',
        ),
        migrations.AddField(
            model_name='tutor',
            name='user_type',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]