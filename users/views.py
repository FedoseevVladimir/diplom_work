from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from school.models import MyCourses


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return redirect('index')
    else:
        form = UserLoginForm()
    context = {
        'form': form,
    }
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)


@login_required(login_url='/users/login/')
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user)
    context = {
        'form': form,
        'my_courses': MyCourses.objects.filter(user=user)
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return redirect('index')
