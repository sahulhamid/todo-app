from django import forms

from django.contrib.auth.models import User

from .models import Todo


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class DateInput(forms.DateInput):
    input_type="datetime-local"

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields='__all__'
        widgets={
        'tasked':DateInput()
        }

