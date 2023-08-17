from django.views.generic import ListView

from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from lifters.models import UserProfile

from feed.models import Feed, Post

def home_view(request):
    if request.user.is_authenticated:
        user_feed = Feed.objects.filter(user=request.user).first()
        return render(request, 'home.html', {'user_feed':user_feed.items.all()})
    else:
        return render(request, 'index.html', {'is_index':True})


class search_view(ListView):
    model = UserProfile
    template_name = "search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        profile_list = UserProfile.objects.filter(
            Q(name__icontains=query) | Q(bio__icontains=query)
        )
        post_list = Post.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

        object_list = [profile_list, post_list]
        return object_list
