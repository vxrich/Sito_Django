# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/contacts.html')

def gallery(request):
    return render(request, 'personal/gallery.html')

def mission(request):
    return render(request, 'personal/mission.html')