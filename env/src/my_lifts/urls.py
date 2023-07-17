"""my_lifts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from lifters import views as lifters_views
from pages import views as pages_views
from API import views as API_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', lifters_views.user_list, name='user_list'),
    path('', pages_views.home_view, name='home'),
    path('search/', pages_views.search_view.as_view(), name='search'),
    path('', include('authentication.urls', namespace='auth')),
    path('profile/', include('lifters.urls', namespace='profile')),
    path('records/', include('records.urls', namespace='record')),
    path('feed/', include('feed.urls', namespace='feed')),

    # API endpoints
    path('all-users/', API_views.UserList.as_view()),
]
