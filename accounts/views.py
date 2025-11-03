from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserRegisterForm, AdminRegisterForm, LoginForm

def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form, 'title': 'Регистрация пользователя'})

def register_admin(request):
    if request.method == 'POST':
        form = AdminRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = AdminRegisterForm()
    return render(request, 'accounts/register_admin.html', {'form': form, 'title': 'Регистрация администратора'})

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = LoginForm

class UserLogoutView(LogoutView):
    next_page = '/'
