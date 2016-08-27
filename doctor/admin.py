from django.contrib import admin
from doctor.models import Patient,RegisterDevicesForPatient,InsuranceCompany
from django import forms




class DeviceRegistationAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    search_fields = ['id']
    fields = ('Patient_ID','SugarMonitoringDevice','WorkOutMachineDevice','PulseMonitor','TemperatureMonitor','SleepPatternsMonitor')
    list_display = ('id', 'patient_name','SugarMonitoringDevice','WorkOutMachineDevice','PulseMonitor','TemperatureMonitor','SleepPatternsMonitor','SleepPatternsDeviceID')
    model = RegisterDevicesForPatient

    def patient_name(self, instance):
        return instance.Patient_ID.FullName
    list_per_page = 10



class PatientAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    search_fields = ['id']
    fields = ('Patient_ID','FullName','FullAddress')
    list_display = ('Patient_ID','FullName','FullAddress','Patient_History','DoctorID','InsuranceCompanyID','RegisterPatientRemoteMonitoring')
    model = Patient

    def patient_name(self, instance):
        return instance.Patient_ID.FullName
    list_per_page = 10


admin.site.register(InsuranceCompany)
admin.site.register(Patient,PatientAdmin)
admin.site.register(RegisterDevicesForPatient,DeviceRegistationAdmin)