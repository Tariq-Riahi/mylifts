from django.urls import path

from .feeds import LatestRecordsFeed

app_name = 'feed'
urlpatterns = [
    path('latest/', LatestRecordsFeed()),
]