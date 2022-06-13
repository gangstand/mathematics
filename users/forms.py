from django import forms
from django.forms import TextInput, EmailInput
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'group', 'password1', 'password2')
        widgets = {
            'first_name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Имя',
                }
            ),
            'last_name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Фамилия',
                }
            ),
            'group': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Группа',
                }
            ),
            'email': EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Почта',
                }
            ),
            'username': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Обращение',
                }
            ),

            'password1': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Обращение',
                }
            ),

            'password2': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Обращение',
                }
            ),
        }


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'group',)
