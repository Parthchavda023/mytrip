from django import forms
from .models import *

class signupForm(forms.ModelForm):
    class Meta:
        model = signupModel
        fields = '__all__'

class updateForm(forms.ModelForm):
    class Meta:
        model = signupModel
        fields = ['id', 'firstname', 'lastname', 'username', 'password', 'state', 'city', 'number']
    
class tripForm(forms.ModelForm):
    class Meta:
        model = tripModel
        fields = '__all__'