from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from feed.models import Post

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

