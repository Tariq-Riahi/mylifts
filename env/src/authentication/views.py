from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm

from lifters.models import *

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Could not log the user in. Make sure the username and password are correct.")
            return redirect('auth:login')
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "You have succesfully logged out.")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration was succesful")
            profile_obj = UserProfile(
                name = form.cleaned_data['username'],
                user = user,
            )
            profile_obj.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {
        'form': form,
    })