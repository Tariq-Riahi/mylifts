from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import RecordCreateForm
from .models import Record


@login_required
def record_create_view(request):
    user = request.user
    form = RecordCreateForm(request.POST or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = user
        obj.save()
        return redirect("profile:details", profile_user_id=user.id)

    context = {
        'form': form,
    }

    return render(request, "create_record.html", context)

@login_required
def record_edit_view(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    if not record.has_change_permission(request):
        return redirect("profile:details", profile_user_id=request.user.id)
    if request.method == 'GET':
        context = {'form': RecordCreateForm(instance=record), 'record_id':record_id}
        return render(request,"create_record.html", context)
    elif request.method == 'POST':
        form = RecordCreateForm(request.POST, instance=record)
        form.save()
        return redirect("profile:details", profile_user_id=request.user.id)
    else:
        return render(request, "create_record.html", {'form':form})

@login_required
def record_delete_view(request, record_id):
    record = get_object_or_404(Record, id=record_id)

    if record.has_change_permission(request):
        record.delete()

    return redirect("profile:details", profile_user_id=request.user.id)
