from django.urls import path

from .feeds import LatestRecordsFeed
from .views import *

app_name = 'feed'
urlpatterns = [
    path('add/', create_post_view, name='add'),
    path('<int:post_id>/', details_post_view, name='post-details'),
    path('like/<int:post_id>', like_toggle, name='like'),
]