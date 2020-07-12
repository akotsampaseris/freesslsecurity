from django import forms

from .models import User

class LoginForm(forms.Form):
    email=forms.EmailField(required=True)
    password=forms.CharField(widget=forms.PasswordInput(), required=True)


class RegisterForm(forms.ModelForm):
    email=forms.EmailField(required=True)
    password=forms.CharField(widget=forms.PasswordInput(), required=True)
    confirm_password=forms.CharField(widget=forms.PasswordInput(), required=True)
    class Meta:
        model = User
        fields = ['email', 'password']


class EditUserForm(forms.ModelForm):
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['email', 'password']
