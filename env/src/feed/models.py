from django.db import models

from django.contrib.auth.models import User

from records.models import Record
from lifters.models import UserProfile


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    title = models.TextField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    date = models.DateField()
    likes = models.ManyToManyField(User, related_name='likers', default=[])

class Feed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Post, null=True, blank=True)

class RecordPost(Post):
    item = models.ForeignKey(Record, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(blank=False, null=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date = models.DateField()
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)


