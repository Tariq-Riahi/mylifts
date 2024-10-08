from django.urls import path

from .import views

app_name = 'profile'
urlpatterns = [
    path('<pk>/', views.profile_detail_view.as_view(template_name='profile_detail.html'), name='details'),
    path('follow_toggle/<int:profile_id>', views.follow_toggle, name='follow-toggle'),
    path('<int:profile_id>/followers', views.followers_list, name='followers'),
    path('<int:profile_id>/following', views.following_list, name='following'),
]