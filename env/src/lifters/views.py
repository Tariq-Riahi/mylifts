import datetime

from django.shortcuts import render, get_object_or_404

from .models import *
from records.models import Record
from records.choices import lift_names


def user_list(request):
    users = UserProfile.objects.all()
    return render(request, 'user_list.html', {'users': users})

def profile_detail_view(request, profile_user_id):
    # get profile objects
    profile_user = get_object_or_404(User, id=profile_user_id)
    profile = get_object_or_404(UserProfile, user=profile_user)
    own_profile = profile_user == request.user

    # get records
    personal_record = get_object_or_404(PersonalRecord, user=profile_user)
    records = Record.objects.filter(user=profile_user)

    # get lifetime records
    lifetime_records = get_top_records(records)

    # get latest records
    latest_records = get_latest_records(records)

    # get unit
    unit = "lbs"
    if get_object_or_404(UserProfile, user=request.user).metric:
        unit = "kg"

    context = {
        "profile": profile,
        "own_profile": own_profile,
        "personal_record": personal_record,
        "records": records,
        "lifetime_records": lifetime_records,
        "latest_records": latest_records,
        "unit": unit,
        "lift_names": lift_names,
    }
    
    return render(request, "profile_detail.html", context)

def get_top_records(records):
    res = []
    for lift_name in lift_names:
        max_record = None
        max_weight = 0
        for record in records:
            if record.lift_name == lift_name and record.weight_lifted > max_weight:
                max_record = record
                max_weight = record.weight_lifted
        if max_record:
            res.append(max_record)
    return res

def get_latest_records(records):
    res = []
    for lift_name in lift_names:
        last_record = None
        last_date = datetime.date(1,1,1)
        for record in records:
            if record.lift_name == lift_name and record.date_lifted > last_date:
                last_record = record
                last_date = record.date_lifted
        if last_record:
            res.append(last_record)
    return res