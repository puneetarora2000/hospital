from django.contrib import admin
from django import forms
from .models import Appointment, Employee, User,Group

from practitioner.models import Practitioner

# class AppointmentAdmin(admin.ModelAdmin):
#     def get_form(self, request, obj=None, **kwargs):
#         form = super(AppointmentAdmin,self).get_form(self,request, obj, **kwargs)
#         form.base_fields['PatientId'].queryset = User.objects.filter(groups__name='Patients')
#         return form

# Register your models here.
# admin.site.register(Appointment, AppointmentAdmin)

class GroupForm(forms.ModelForm):
    model = Group

class GroupAdmin(admin.ModelAdmin):
    search_fields = ['id','name']
    form = GroupForm
    list_display = ('id', 'name')
    list_per_page = 10

admin.site.unregister(Group)
admin.site.register(Group,GroupAdmin)

# class AppointmentForm(forms.ModelForm):
#     model = Group
#RelatedFieldAdmin
class AppointmentAdmin(admin.ModelAdmin):
     empty_value_display = '-empty-'
    search_fields = ['id','DateOfAppointment']
    list_display = ('id', 'emp_name', 'Remarks')

    def emp_name(self, instance):
        return instance.EmployeeID.Employee_Name

    def patient_name(self, instance):
        return instance.PatientId.username

    list_per_page = 10

admin.site.register(Appointment,AppointmentAdmin)