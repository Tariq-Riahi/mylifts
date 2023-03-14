from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(null=True, blank=True, upload_to="images/")
    tiktok_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    youtube_url = models.URLField(max_length=255, blank=True, null=True)
    # Add other fields as necessary


class PersonalRecord(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    lift_name = models.CharField(max_length=100)
    weight_lifted = models.DecimalField(max_digits=5, decimal_places=2)
    date_lifted = models.DateField()
    video_url = models.URLField(blank=True, null=True)
    # Add other fields as necessary
