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
        "comments":comments
    })

@login_required
def like_post(request, blog_id):
    
    like = Like.objects.create(
    is_like=True,
    blog_id=blog_id,
    user_id=request.user
    )
    like.save()

    return redirect('index')