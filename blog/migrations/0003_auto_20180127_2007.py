# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-27 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(upload_to='blog/cover'),
        ),
    ]