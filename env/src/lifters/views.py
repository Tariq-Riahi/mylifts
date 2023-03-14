from django.shortcuts import render

from .models import *


def user_list(request):
    users = UserProfile.objects.all()
    return render(request, 'user_list.html', {'users': users})
