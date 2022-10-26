from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer

class LoginForm(forms.Form):   
    account = forms.CharField()

class RegistrationForm(forms.ModelForm):   
    account = forms.CharField()
    name    = forms.CharField    
    phone   = forms.CharField()
    age     = forms.IntegerField()
    address = forms.CharField()
    balance = forms.DecimalField()
    
    class Meta:
        model = Customer
        fields = ['account','name','phone','age','address','balance']

class OptionsForm(forms.Form):
    choice  = forms.ChoiceField(choices = (("Debit","Debit"),("Credit","Credit")))

class CreditForm(forms.Form):
    source      = forms.CharField()
    amount      = forms.DecimalField()
    destination = forms.CharField()


class DebitForm(forms.Form):
    account = forms.CharField()
    value   = forms.DecimalField()
