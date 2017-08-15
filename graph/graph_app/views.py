# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm# Create your views here.
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.contrib.auth.decorators import login_required,user_passes_test 

def index(request):
    if request.user.is_anonymous():
       print "-----------"
       return render(request, 'index.html')
    else:
        return HttpResponseRedirect(reverse('dashboard'))

def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return HttpResponseRedirect(reverse('index'))
    else:
        f = UserCreationForm()
    print f
    return render(request, 'signup.html', {'form': f})

@login_required
def dashboard(request):
    return render(request,'dashboard.html')