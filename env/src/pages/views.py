from django.views.generic import ListView

from django.shortcuts import render
from django.db.models import Q

from lifters.models import UserProfile

def home_view(request):
    return render(request, 'home.html', {})

class search_view(ListView):
    model = UserProfile
    template_name = "search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = UserProfile.objects.filter(
            Q(name__icontains=query) | Q(bio__icontains=query)
        )
        return object_list
