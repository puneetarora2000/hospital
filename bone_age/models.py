from __future__ import unicode_literals
from django.db import models
from time import time
from time import time
import random
import string
from doctor.models import Patient


class BoneAgeAssessmentPatient(models.Model):
    Patient_ID = models.ForeignKey(Patient, default=1, blank=True)
    Measurement = models.FloatField()
    def __unicode__(self):
        return str(self.Patient_ID)
