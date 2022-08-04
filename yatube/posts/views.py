from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from posts.forms import PostForm
from posts.models import Group, Post

User = get_user_model()


def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        'page': page,
        'paginator': paginator,
    }
    return render(request, 'posts/index.html', context)


def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = user.posts.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        'user': user,
        'page': page,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, username, post_id):
    user = get_object_or_404(User, username=username)
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'user': user,
        'post': post,
    }
    return render(request, 'posts/post_detail.html', context)


def group_list(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        'group': group,
        'paginator': paginator,
        'page': page,
    }
    return render(request, 'posts/group_list.html', context)


@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:index')
        return render(request, "posts/post_create.html", {"form": form})
    form = PostForm()
    return render(request, "posts/post_create.html", {"form": form})


def post_edit(request, username, post_id):
    is_edit = get_object_or_404(Post, pk=post_id)
    if is_edit.author == request.user:
        if request.method == "POST":
            form = PostForm(request.POST, instance=is_edit)
            if form.is_valid():
                form.save()
                return redirect('posts:post_detail', username, post_id)
        form = PostForm(instance=is_edit)
        return render(
            request,
            "posts/post_create.html",
            {
                "form": form,
                "username": username,
                "post_id": post_id,
                "is_edit": is_edit
            }
        )
    return redirect('posts:post_detail', username, post_id)
