from django.shortcuts import render, get_object_or_404, redirect

from .forms import CommentForm
from .models import Post, Comment, Tag, Resume
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse


def home_page(request):
    posts = Post.objects.all().order_by('-created')[:6]
    context = {'posts': posts}
    return render(request, 'index.html', context)


def gallery_page(request):
    posts = Post.objects.all().order_by('-created')
    context = {'posts': posts}
    return render(request, 'gallery.html', context)


def gallery_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('gallery_detail', pk=pk)
    else:
        form = CommentForm()

    comments = post.comment_set.all()  # Fetch comments associated with the post
    context = {'post': post, 'form': form, 'comments': comments}
    return render(request, 'single.html', context)


def resume_page(request, pk):
    posts = Resume.objects.all()
    context = {'resumes': posts, }
    return render(request, 'about.html', context)


def about_page(request):
    posts = Post.objects.all().order_by('-created')[:1]
    context = {'about': posts}
    return render(request, 'about.html', context)


# def detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     comments = Comment.objects.filter(post=post).order_by('-created')
#
#     if request.method == 'POST':
#         form = CommentForm(request.POST, request.FILES)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.save()
#             return redirect('detail', pk=pk)
#     else:
#         form = CommentForm()
#
#     context = {'post': post, 'comments': comments, 'form': form}
#     return render(request, 'single.html', context)

# def detail(request, pk, *args, **kwargs):
#     form = CommentForm()
#     post = get_object_or_404(Post, pk=pk)
#     comments = Comment.objects.filter(post__id=pk).order_by('-created')
#     if request.method == 'POST':
#         form = CommentForm(request.POST, request.FILES)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.save()
#             return redirect(f'detail/{post.id}')
#     context = {'form': form,
#                'articles': post,
#                'comments': comments}
#     return render(request, 'single.html', context)

# views.py


# from .forms import CommentForm


def submit_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('gallery_detail', pk=pk)
    else:
        form = CommentForm()

    # Retrieve comments associated with the post
    comments = post.comment_set.all()

    context = {'post': post, 'form': form, 'comments': comments}
    return render(request, 'single.html', context)


from django.utils import timezone


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.created = timezone.now()
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form})
