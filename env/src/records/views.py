from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import RecordCreateForm


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

