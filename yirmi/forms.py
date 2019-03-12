from django import forms

from django.contrib.auth.forms import UserCreationForm
from .models import User, Report, Department

class UserForm(UserCreationForm):
    username = forms.CharField(max_length=30,label="Kullanıcı adı") 
    first_name = forms.CharField(max_length=30,label="İsim" )
    last_name = forms.CharField(max_length=30, label="Soyisim")
    email = forms.EmailField(max_length=254, help_text='Zorunlu. Lütfen geçerli bir e-mail adresi veriniz.',)
    username.widget.attrs.update({'class':'form-group-special col-10 float-right'})
    username.widget.label_classes = ('col-2', 'float-left' )
    first_name.widget.attrs.update({'class':'form-group-special col-10 float-right'})
    last_name.widget.attrs.update({'class':'form-group-special col-10 float-right'})
    email.widget.attrs.update({'class':'form-group-special col-10 float-right'})
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
    def __init__(self, *args, **kwargs): 
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].label_class = ('col-2', 'class_b' )
        
    
        
class ReportForm(forms.ModelForm):
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    class Meta:
        model = Report
        fields = [
            'header',
            'text',
            'department',
            ]    
           
