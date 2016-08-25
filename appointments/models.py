
from __future__ import unicode_literals
from django.db import models
from time import time

from employee.models import *

class Appointment(models.Model):
    EmployeeID = models.ForeignKey(Employee,default=5, limit_choices_to={'groups__id':2})
    PatientId = models.ForeignKey(User,default=1, limit_choices_to={'groups__id':1})
    DateOfAppointment = models.DateField(auto_now=False,auto_now_add=False)
    Remarks = models.TextField(verbose_name='Remarks or Comments',max_length='300')

    def __unicode__(self):
        return self.Remarks
          

	
