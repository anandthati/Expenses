# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm# Create your views here.
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.contrib.auth.decorators import login_required,user_passes_test 
from django.http import JsonResponse

from .forms import AddExpensesForm,AddIncomeForm
from .models import AddExpenses,AddIncome
def index(request):
    if request.user.is_anonymous():
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

@login_required
def summary(request):
    expenses = AddExpenses.objects.filter(owner=request.user)
    income = AddIncome.objects.filter(owner=request.user)
    return render(request,'summary.html',{'expenses':expenses,'income':income})

@login_required
def addexpense(request):
    if request.method == 'POST':
        form = AddExpensesForm(request.POST)
        print "form : ", request.POST.get('amount'),request.POST.get('date'),request.POST.get('owner'),request.POST.get('purpose')
        if form.is_valid():
            form.save() 
        else:
            print "not valid"           
    
    args={}
    args['form'] = AddExpensesForm(initial={'owner':request.user})
    return render(request,'addexpense.html',args,{'foo':'expense'})

@login_required
def addincome(request):
    if request.method == 'POST':
        form = AddIncomeForm(request.POST)
        print "form : ", request.POST.get('amount'),request.POST.get('date'),request.POST.get('owner'),request.POST.get('purpose')
        if form.is_valid():
            form.save() 
        else:
            print "not valid"           
    
    args={}
    args['form'] = AddIncomeForm(initial={'owner':request.user})
    return render(request,'addincome.html',args)
