# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-27 14:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=b''),
            preserve_default=False,
        ),
    ]
