from django import forms
from .models import Contact,Login


class LoginForm(forms.ModelForm):
    model = Login
    fields = ['username','password']
    widgets = {
            'username': forms.TextInput(
                attrs={'required': True, "placeholder": "Username"}
            ),
            'password': forms.TextInput(
                attrs={'required': True, 'placeholder': "Password"}
            ),
        }