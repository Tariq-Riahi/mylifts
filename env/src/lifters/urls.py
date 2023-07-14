from django.urls import path

from .import views

app_name = 'profile'
urlpatterns = [
    path('<pk>/', views.profile_detail_view.as_view(template_name='profile_detail.html'), name='details'),
    # path('<int:profile_user_id>/', views.profile_detail_view.as_view(), name='details'),
    path('follow_toggle/<int:profile_user_id>', views.follow_toggle, name='follow-toggle'),
]