from django.contrib import admin
from django.contrib.auth.models import Group

from django import forms





# class GroupForm(forms.ModelForm):
#     model = Group
#
# class GroupAdmin(admin.ModelAdmin):
#     search_fields = ['id','group']
#     form = GroupForm
#     list_display = ('id', 'group')
# list_per_page = 3
#
# admin.site.unregister(Group)
# admin.site.register(Group,GroupAdmin)