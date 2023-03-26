from django.urls import path

from .import views

app_name = 'record'
urlpatterns = [
    path('add/', views.record_create_view, name='add'),
]