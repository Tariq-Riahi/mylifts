from django.urls import path

from .import views

app_name = 'profile'
urlpatterns = [
    path('<int:profile_user_id>/', views.profile_detail_view, name='details'),
]