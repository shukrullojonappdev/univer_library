from django import forms

class RegistrationForm(forms.Form):
  username = forms.CharField(50, label='Username')
  email = forms.EmailField(100, label='Email')
  password = forms.CharField(100, label='Password')