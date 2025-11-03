from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class UserRegisterForm(UserCreationForm):
    phone = forms.CharField(label='Телефон')
    birth_date = forms.DateField(label='Дата рождения', widget=forms.DateInput(attrs={'type': 'date'}))
    city = forms.CharField(label='Город')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'birth_date', 'city', 'password1', 'password2']

class AdminRegisterForm(UserCreationForm):
    phone = forms.CharField(label='Телефон')
    birth_date = forms.DateField(label='Дата рождения', widget=forms.DateInput(attrs={'type': 'date'}))
    city = forms.CharField(label='Город')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'birth_date', 'city', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True
        user.is_superuser = True
        user.is_admin_user = True
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
