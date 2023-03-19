from django.shortcuts import render, get_object_or_404

from .models import *


def user_list(request):
    users = UserProfile.objects.all()
    return render(request, 'user_list.html', {'users': users})

def profile_detail_view(request, profile_user_id):
    profile_user = get_object_or_404(User, id=profile_user_id)
    profile = get_object_or_404(UserProfile, user=profile_user)
    own_profile = profile_user == request.user

    personal_record = get_object_or_404(PersonalRecord, user=profile_user)

    unit = "lbs"
    if get_object_or_404(UserProfile, user=request.user).metric:
        unit = "kg"

    context = {
        "profile": profile,
        "own_profile": own_profile,
        "personal_record": personal_record,
        "unit": unit,
    }
    
    return render(request, "profile_detail.html", context)


