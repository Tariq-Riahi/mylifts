from django.conf import settings
from django.contrib.auth.models import User

from datetime import date, timedelta

from feed.models import Feed, Post
from lifters.models import UserProfile


def schedule_following_feed_updater():
    print("Starting job")
    feeds = Feed.objects.all()

    items = Post.objects.all()
    items_new = items.order_by('date')

    today = date.today()
    startdate = today - timedelta(days=1)
    items_popular = items.filter(date__range=[startdate, today]).order_by('date')[:100]
    # Creating personalized feeds for the users
    for feed in feeds:
        user = feed.user
        user_profile = UserProfile.objects.all().filter(user=user).first()
        user_following = user_profile.following.all().values_list('user', flat=True)

        feed_items = []
        for item in items_new[:100]:
            if user != item.user and (item.user.id in user_following):
                feed_items.append(item)
        feed.items.set(feed_items, clear=True)
        feed.save()




def schedule_popular_feed_updater():
    # Creating the popular feed
    popular_user = User.objects.all().filter(username="popular").first()
    popular_feed = Feed.objects.all().filter(user=popular_user).first()
    popular_feed.items.set(items_popular, clear=True)


