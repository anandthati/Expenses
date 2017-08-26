# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class AddExpenses(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	amount = models.BigIntegerField(default=0)
	purpose = models.CharField(max_length=255,default='personal')
	date = models.DateField(null=True, blank=True)

class AddIncome(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	amount = models.BigIntegerField(default=0)
	source = models.CharField(max_length=255,default='salary')
	date = models.DateField(null=True, blank=True)
