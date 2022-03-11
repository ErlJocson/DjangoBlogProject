from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *

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
    return render(request, 'blog_comment.html', {})