from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from datetime import date

from feed.models import Post
from lifters.models import UserProfile
from feed.forms import *

@login_required
def like_toggle(request, post_id):
    post_obj = get_object_or_404(Post, id=post_id)
    likes = post_obj.likes.all()
    user = request.user

    if user in likes:
        post_obj.likes.remove(user)
    else:
        post_obj.likes.add(user)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def create_post_view(request):
    form = RecordPostCreateForm(request.POST or None, user=request.user)
    # form = RecordPostCreateForm(request.POST or None)
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.date = date.today()
        # obj.likes = 0
        obj.save()
        return redirect("profile:details", pk=user_profile.id)

    context = {
        'form': form,
    }

    return render(request, "post_create.html", context)

def details_post_view(request, post_id):
    post_obj = get_object_or_404(Post, id=post_id)
    liked_by_user = request.user in post_obj.likes.all()

    context = {
        'post': post_obj,
        'liked_by_user': liked_by_user,
    }

    return render(request, "post_detail.html", context)