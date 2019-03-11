from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Report, Department

class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password',  'is_activated')

class UserAdmin(UserAdmin):
    form = UserChangeForm


# Register your models here.
admin.site.register(User,UserAdmin)

admin.site.register(Report)
admin.site.register(Department)