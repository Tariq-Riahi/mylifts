from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Record(models.Model):
    # id = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lift_name = models.CharField(max_length=100)
    weight_lifted = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    body_weight = models.PositiveIntegerField(blank=True, null=True)
    date_lifted = models.DateField()
    video_url = models.URLField(blank=True, null=True)