from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User

class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        return Response(users.values())
