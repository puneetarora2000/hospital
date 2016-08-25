from django.contrib.auth.models import User, Group
from appointments.models import  Appointment
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
class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  Appointment
        fields = ('EmployeeID','PatientId','DateOfAppointment','Remarks')

#