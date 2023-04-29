from django.urls import path

from .import views

app_name = 'record'
urlpatterns = [
    path('add/', views.record_create_view, name='add'),
    path('edit/<int:record_id>/', views.record_edit_view, name='edit'),
    path('delete/<int:record_id>/', views.record_delete_view, name='delete'),
]