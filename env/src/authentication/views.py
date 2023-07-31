from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from datetime import date

from .forms import RegisterForm

from lifters.models import *
from feed.models import Feed, Post

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
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            init_user(user, form)
            init_feed(user)
            messages.success(request, "Registration was succesful")
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {
        'form': form,
    })

def init_user(user, form):
    # Create a UserProfile object
    age = calculate_age(form.cleaned_data["date_of_birth"])
    metric = form.cleaned_data['metric']
    profile_obj = UserProfile(
        name=form.cleaned_data['username'],
        user=user,
        age = age,
        metric=metric,
        profile_picture='images/download.png'
    )
    profile_obj.save()

    # Create a PersonalRecord object
    pr_obj = PersonalRecord(
        user=user,
    )
    pr_obj.save()


def init_feed(user):
    items = Post.objects.all().order_by('likes')[:20]
    feed = Feed.objects.create(
        user = user
    )
    feed.items.set(items)
    feed.save()

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))