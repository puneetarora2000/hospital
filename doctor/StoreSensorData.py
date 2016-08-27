from django.db.models.expressions import F

from doctor.models import *
from doctor.dataproviders import *
from faker import Factory
from autofixture import AutoFixture
from django.contrib.auth.models import User,Group
from datetime import datetime
from django.utils import timezone
import random

def insertSubject():
    fake = Factory.create()
    for num in range(1,10):
        DoctorUserID = User.objects.filter(groups__id=5).order_by('?').first()
        InsuranceCompanyID = InsuranceCompany.objects.order_by('?').first()
        patient = Patient(Patient_ID=random.randint(12,111111),FullName=fake.name(),FullAddress=fake.address(),\
                          Patient_History=fake.text(),RegisterPatientRemoteMonitoring="True",Credential="",\
                          DoctorID=DoctorUserID,InsuranceCompanyID=InsuranceCompanyID)
        patient.save()
        print("----done--------")


def insertDeviceReg():
    fake = Factory.create()
    for num in range(2,90):
        Patient_ID = Patient.objects.order_by('?').first()
        patient = RegisterDevicesForPatient(Patient_ID=Patient_ID,SugarMonitoringDevice=False,WorkOutMachineDevice=True\
                                            ,PulseMonitor=False,TemperatureMonitor=False,SleepPatternsMonitor=True)

        patient.save()
        print("----done Registrations--------"+str(Patient_ID.pk))

def insertPatientHealth(count):
    fake = Factory.create()
    for num in range(1,count):
        # Get patients id's list
        Patient_list = Patient.objects.values_list('id', flat=True)
        # Filter those patients which are added as a foreign key to registerdevicesforpatient model and get a single random value
        Patient_object = Patient.objects.filter(registerdevicesforpatient__Patient_ID__in = Patient_list).order_by('?').first()
        year = random.choice(range(2015, 2016))
        month = random.choice(range(1, 12))
        day = random.choice(range(1, 29))
        date_of_reading = datetime(year, month, day)
        timezone_date = timezone.make_aware(date_of_reading, timezone.get_current_timezone())
        InsuranceCompanyID = InsuranceCompany.objects.order_by('?').first()
        health_data = PatientHealthData(Patient_ID=Patient_object,InsuranceCompanyID=InsuranceCompanyID, \
                                        WorkOutMachineDeviceReading=random.randint(20,60), \
                                        SleepPatternsMonitorReading=random.randint(360,720),DataOfReading=timezone_date)
        health_data.save()
        print("----Added Patient Health Data--------")