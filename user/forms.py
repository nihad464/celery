from file.models import ShareModel
from django.forms import ModelForm
from .models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm
class LoginForm(forms.Form):
    email=forms.CharField(label='email',
                    widget=forms.EmailInput(attrs={'placeholder':'email'}))
    username= forms.CharField(label='username', 
                    widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password= forms.CharField(label='parol', 
                    widget=forms.PasswordInput(attrs={'placeholder': 'password'}))

class RegisterForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=['first_name','last_name','username','email','password1','password2','avatar']
        widgets = {
        'first_name': forms.fields.TextInput(attrs={'placeholder': 'first_name'}),

        'username': forms.fields.TextInput(attrs={'placeholder': 'last_name'}),

        'username': forms.fields.TextInput(attrs={'placeholder': 'username'}),

        'email': forms.fields.TextInput(attrs={'placeholder': 'email stuff'})
        }
class AllowerForm(forms.ModelForm):
    class Meta:
        model=ShareModel
        fields='__all__'
        exclude=['sender']
