from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Blog, Comment, Like

@login_required
def index_view(request):
    blogs = Blog.objects.all()

    if request.method == "POST":

        try:
            content = request.POST['content']
        except:
            content = ''
            
        if content:
            blog_to_save = Blog.objects.create(
                content=content,
                user_id=request.user
            )
            blog_to_save.save()
            messages.success(request, "New blog uploaded!")

    return render(request, "index.html", {
        "title":"Home",
        "blogs":blogs
    })

@login_required
def blog_comment_view(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    comments = Comment.objects.filter(blog_id=blog_id)
    likes = Like.objects.filter(blog_id=blog_id)
    liked = False

    for i in likes:
        if request.user == i.user_id:
            liked = True

    if request.method == "POST":
        
        try:
            content = request.POST['content']
        except:
            content = ''
        
        if content:
            comment_to_save = Comment.objects.create(
                content=content,
                blog_id=blog,
                user_id=request.user
            )
            comment_to_save.save()
            messages.success(request, "You have commented!")

    return render(request, 'blog_comment.html', {
        "title":"Comments",
        "blog":blog,
        "comments":comments,
        "likes":len(likes),
        "liked":liked,
    })

@login_required
def like_post(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    
    check_if_liked = Like.objects.filter(blog_id=blog)

    if not check_if_liked:
        like = Like.objects.create(
            is_like=True,
            blog_id=blog,
            user_id=request.user
        )
        like.save()
        messages.success(request, 'Liked')
    return redirect('comments-likes', blog_id=blog_id)

@login_required
def unlike_post(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    check_if_liked = Like.objects.filter(blog_id=blog)

    if check_if_liked:
        check_if_liked.delete()
        messages.success(request, 'Unliked')

    return redirect('comments-likes', blog_id=blog_id)