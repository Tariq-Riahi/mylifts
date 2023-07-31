from django.urls import path

from .feeds import LatestRecordsFeed
from .views import like_toggle

app_name = 'feed'
urlpatterns = [
    path('latest/', LatestRecordsFeed()),
    path('like/<int:post_id>', like_toggle, name='like'),
]