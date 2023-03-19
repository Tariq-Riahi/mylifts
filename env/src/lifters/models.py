from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

from records.models import Record


class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    weight = models.PositiveIntegerField(blank=True, null=True)
    profile_picture = models.ImageField(null=True, blank=True, upload_to="images/")
    tiktok_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    youtube_url = models.URLField(max_length=255, blank=True, null=True)
    metric = models.BooleanField()


class PersonalRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    benchpress = models.ForeignKey(Record, null=True, on_delete=models.SET_NULL)
    # lift_name = models.CharField(max_length=100)
    # weight_lifted = models.DecimalField(max_digits=5, decimal_places=2)
    # date_lifted = models.DateField()
    # video_url = models.URLField(blank=True, null=True)
