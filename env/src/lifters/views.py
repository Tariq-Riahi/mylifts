import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView

from .models import *
from records.models import Record
from records.choices import lift_names


def user_list(request):
    users = UserProfile.objects.all()
    return render(request, 'user_list.html', {'users': users})

class profile_detail_view(DetailView):
    model = UserProfile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_own_profile'] = self.object.user == self.request.user
        context['own_profile'] = get_object_or_404(UserProfile, user=self.request.user)

        # get records
        context['personal_record'] = get_object_or_404(PersonalRecord, user=self.object.user)
        context['records'] = Record.objects.filter(user=self.object.user)

        # get lifetime records
        context['lifetime_records'] = get_top_records(context['records'])

        # get latest records
        context['latest_records'] = get_latest_records(context['records'])

        # get unit
        if self.object.metric:
            context['unit'] = "kg"
        else:
            context['unit'] = "lbs"

        return context


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

def follow_toggle(request, profile_user_id):
    profile_user_obj = get_object_or_404(User, id=profile_user_id)
    profile_obj = get_object_or_404(UserProfile, user=profile_user)
    current_user_obj = get_object_or_404(UserProfile, user=request.user)
    following = profile_obj.following.all()

    if lifter_obj != current_user_obj:
        if current_user_obj in following:
            lifter_obj.following.remove(current_user_obj.user.id)
        else:
            lifter_obj.following.add(current_user_obj.user.id)

    return HttpResponseRedirect(reverse(profile_detail_view, args=[profile_user_id]))

