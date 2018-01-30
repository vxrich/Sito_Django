# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from PIL import Image

class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()
    cover = models.ImageField(upload_to="static/cover/")

    def __str__(self):
        return self.title
