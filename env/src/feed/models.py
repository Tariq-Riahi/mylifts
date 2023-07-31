from django.db import models

from django.contrib.auth.models import User

from records.models import Record
from lifters.models import UserProfile


class Post(models.Model):
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    likes = models.ManyToManyField(User)

class Feed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Post)

class RecordPost(Post):
    item = models.ForeignKey(Record, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(blank=False, null=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date = models.DateField()
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)


