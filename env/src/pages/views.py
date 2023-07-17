from django.views.generic import ListView

from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from lifters.models import UserProfile

from records.models import Record

def home_view(request):
    user_profiles = get_object_or_404(UserProfile, user=request.user)
    following = user_profiles.following.all()
    users = [user_profile.user for user_profile in following]
    print(users)
    records = Record.objects.all().filter(user__in=users)
    return render(request, 'home.html', {'records':records})

class search_view(ListView):
    model = UserProfile
    template_name = "search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = UserProfile.objects.filter(
            Q(name__icontains=query) | Q(bio__icontains=query)
        )
        return object_list
