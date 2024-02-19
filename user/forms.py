from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm

class LoginForm(AuthenticationForm):
    
    class Mete:
        model = User
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=False)
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        

class CustomPasswordResetForm(PasswordResetForm):
    # Add any customizations if needed
    pass