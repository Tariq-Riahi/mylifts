from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import RecordCreateForm
from .models import Record
from lifters.models import UserProfile


@login_required
def record_create_view(request):
    user = request.user
    form = RecordCreateForm(request.POST or None)
    user_profile = get_object_or_404(UserProfile, user=user)
    metric = user_profile.metric

    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = user
        if metric:
            obj.weight_lifted = kg_to_lbs(obj.weight_lifted)
            obj.body_weight = kg_to_lbs(obj.body_weight)
        obj.save()
        return redirect("profile:details", pk=user_profile.id)

    context = {
        'form': form,
    }

    return render(request, "create_record.html", context)

@login_required
def record_edit_view(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    user_profile = get_object_or_404(UserProfile, user=request.user)
    if not record.has_change_permission(request):
        return redirect("profile:details", pk=user_profile.id)
    if request.method == 'GET':
        form = RecordCreateForm(instance=record)
        if user_profile.metric:
            form.initial['weight_lifted'] = int(lbs_to_kg(form.initial['weight_lifted']))
            form.initial['body_weight'] = int(lbs_to_kg(form.initial['body_weight']))
        context = {'form': form, 'record_id':record_id}
        return render(request,"create_record.html", context)
    elif request.method == 'POST':
        form = RecordCreateForm(request.POST, instance=record)
        obj = form.save(commit=False)
        if user_profile.metric:
            obj.weight_lifted = int(kg_to_lbs(obj.weight_lifted))
            obj.body_weight = int(kg_to_lbs(obj.body_weight))
        obj.save()
        return redirect("profile:details", pk=user_profile.id)
    else:
        return render(request, "create_record.html", {'form':form})

@login_required
def record_delete_view(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if record.has_change_permission(request):
        record.delete()

    return redirect("profile:details", pk=user_profile.id)

def record_details_view(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    profile = get_object_or_404(UserProfile, user=record.user)
    context = {
        'record': record,
        'is_own_profile': request.user == record.user,
        'profile': profile,
    }
    return render(request, 'record_details.html', context)

def lbs_to_kg(lbs):
    return round(lbs / 2.205, 0)

def kg_to_lbs(kg):
    return round(kg * 2.205, 0)
