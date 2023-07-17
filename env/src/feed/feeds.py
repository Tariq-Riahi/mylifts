from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.shortcuts import get_object_or_404


from lifters.models import UserProfile
from records.models import Record

class LatestRecordsFeed(Feed):
    title = "Latest Records"
    link = "/latest_records"
    description = "The latest records of all lifters."

    def items(self):
        return Record.objects.order_by("date_lifted")

    def item_title(self, item):
        return item.lift_name

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        user = item.user
        profile_id = get_object_or_404(UserProfile, user=user).id
        return reverse('home')
        # return reverse('profile:details', profile_id)

