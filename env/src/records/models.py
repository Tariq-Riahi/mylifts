from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

from .choices import *

class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lift_name = models.CharField(choices=lift_name_choices, max_length=50)
    weight_lifted = models.DecimalField(max_digits=5, decimal_places=1)
    repetitions = models.PositiveIntegerField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    body_weight = models.PositiveIntegerField(blank=True, null=True)
    date_lifted = models.DateField()
    video_url = models.URLField(blank=True, null=True)

    def has_change_permission(self, request):
        return request.user == self.user