# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from .models import Email
from .forms import EmailForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def list(request):
    emails = Email.objects.all()
    return render(request, 'list.html', {'emails': emails})

def add(request):
    if request.POST:
        print 'processing post request...'
        form = EmailForm(request.POST)
        print form
        if form.is_valid():
            print 'saving email'
            form.save()
            emails = Email.objects.all()
            return render(request, 'list.html', {'emails': emails})
    else:
        form = EmailForm()

    args = {}
    args['form'] = form
    return render(request, 'add.html', args)
