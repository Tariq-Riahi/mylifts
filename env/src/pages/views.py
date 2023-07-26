from django.views.generic import ListView

from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from lifters.models import UserProfile

from feed.models import Feed

def home_view(request):
    user_feed = Feed.objects.filter(user=request.user).first()
    return render(request, 'home.html', {'user_feed':user_feed.items.all()})

class search_view(ListView):
    model = UserProfile
    template_name = "search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = UserProfile.objects.filter(
            Q(name__icontains=query) | Q(bio__icontains=query)
        )
        return object_list
