from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User ,Group
from time import time

# Create your models here.

class Employee(models.Model):
	user = models.OneToOneField(User, unique=True,default=6)
	groups = models.ForeignKey(Group,default=2)
	Employee_Name = models.CharField(max_length=254,default='Mona')
	City = models.CharField(max_length=30,default='Chandigarh')
	Province = models.CharField(max_length=50,default='Chandigarh')
	Date_Of_Joining = models.DateField()

	def __unicode__(self):
		return self.user