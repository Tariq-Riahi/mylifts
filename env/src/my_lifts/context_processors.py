from lifters.models import UserProfile

from django.shortcuts import get_object_or_404


def load_global_vars(request):
    if request.user.is_authenticated:
        user_profile = get_object_or_404(UserProfile, user=request.user)
        return {'user_profile': user_profile}
    return {}