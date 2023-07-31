from django.conf import settings
from django.contrib.auth.models import User

from feed.models import Feed, Post

def schedule_feed_updater():
    print("Starting job")
    feeds = Feed.objects.all()

    items = Post.objects.all().order_by('likes')[:20]
    for feed in feeds:
        feed.items.set(items, clear=True)
        feed.save()

    print(items)