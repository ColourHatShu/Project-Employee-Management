from django.core import validators
from django import forms                #important to import
from .models import User                #important to import

class EmployeeRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(render_value = True, attrs={'class':'form-control'}),
        }
