from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Profile
from .forms import PostForm
from django.contrib.auth.models import User

@login_required
def feed(request):
    posts = Post.objects.all().order_by('-created_at')
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('feed')
    else:
        form = PostForm()
    return render(request, 'feed.html', {'posts': posts, 'form': form})

def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = user.post_set.all()
    return render(request, 'profile.html', {'user': user, 'posts': posts})
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from django.contrib import messages

from django.contrib import messages
from django.http import HttpResponseForbidden

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Ensure only the post owner can delete it
    if post.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this post.")

    # Delete the post
    post.delete()

    # Check if the user has any remaining posts
    remaining_posts = Post.objects.filter(user=request.user).exists()

    # Redirect based on the number of remaining posts
    if not remaining_posts:
        messages.success(request, "All your posts have been deleted. Why not create a new one?")
        return redirect('profile', username=request.user.username)
    else:
        messages.success(request, "Post deleted successfully!")
        return redirect('profile', username=request.user.username)



