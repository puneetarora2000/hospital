from django.contrib.auth.models import User, Group
from doctor.models import  RegisterDevicesForPatient,Patient,InsuranceCompany,PatientHealthData
from rest_framework import serializers



#1
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

#2
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
#3
class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  Patient
        fields = ('Patient_ID','FullName','FullAddress','Patient_History','RegisterPatientRemoteMonitoring','Credential','DoctorID','InsuranceCompanyID')

#
class RegisterDevicesForPatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  RegisterDevicesForPatient
        fields = ('Patient_ID','SugarMonitoringDevice','WorkOutMachineDevice','PulseMonitor','TemperatureMonitor','SleepPatternsMonitor','GulcoseMonitoringDeviceID','WorkOutMachineDeviceID','PulseMonitorID','TemperatureMonitorID','SleepPatternsDeviceID')


class InsuranceCompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  InsuranceCompany
        fields = ('InsuranceCompanyName',)

class PatientHealthDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  PatientHealthData
        fields = ('Patient_ID','InsuranceCompanyID','DataOfReading','WorkOutMachineDeviceReading','SleepPatternsMonitorReading')