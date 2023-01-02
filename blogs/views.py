from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost
from .forms import BlogPostFrom


def index(request):
    """The home page for Blog."""
    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)


def post(request, post_id):
    """Page to show the post content."""
    post = BlogPost.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'blogs/post.html', context)


@login_required()
def new_post(request):
    """Make new post"""
    if request.method != "POST":
        form = BlogPostFrom()
    else:
        form = BlogPostFrom(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            form.save()
            return redirect('blogs:index')

    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)


@login_required()
def edit_post(request, post_id):
    """Edit selected post. """
    post = BlogPost.objects.get(id=post_id)
    if post.owner != request.user:
        raise Http404

    if request.method != "POST":
        form = BlogPostFrom(instance=post)
    else:
        form = BlogPostFrom(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:post', post_id=post.id)

    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)
