from django.conf import settings
from django.contrib.auth.models import User

from feed.models import Feed, Post

def schedule_feed_updater():
    print("Starting job")
    feeds = Feed.objects.all()

    items = Post.objects.all().order_by('likes')[:20]
    for feed in feeds:
        user = feed.user
        feed_items = []
        for item in items:
            if user != item.user:
                feed_items.append(item)
        feed.items.set(feed_items, clear=True)
        feed.save()

    print(items)