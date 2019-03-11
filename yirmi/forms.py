from django import forms

from django.contrib.auth.forms import UserCreationForm
from .models import User, Report, Department

class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, )
    last_name = forms.CharField(max_length=30, )
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',            
            'email',
            'password1',
            'password2',            
            ]
class ReportForm(forms.ModelForm):
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    class Meta:
        model = Report
        fields = [
            'header',
            'text',                      
            ]    
           
