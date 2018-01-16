# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
import django.middleware.csrf as csrf
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    csrf.get_token(request)
    return render(request, 'personal/contacts.html')

def email(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                msg = EmailMessage(subject, message, to=['r.grespan6@gmail.com'],)
                msg.send()
                send_mail(subject, message, from_email, ['r.grespan6@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "personal/email.html", {'form': form})

def success(request):
    return HttpResponse('Success! Thank you for your message.')

def gallery(request):
    return render(request, 'personal/gallery.html')

def mission(request):
    return render(request, 'personal/mission.html')