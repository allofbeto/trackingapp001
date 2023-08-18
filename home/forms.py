from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'login-form__input justify-space', 'placeholder': 'USERNAME'}),
            'email': forms.TextInput(attrs={'class': 'form__input justify-space', 'placeholder': 'EMAIL'}),
            'password1': forms.TextInput(attrs={'class': 'form__input justify-space', 'placeholder': 'PASSWORD'}),
        }
