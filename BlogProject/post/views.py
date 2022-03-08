from django.shortcuts import render
from .models import Blog

def index_view(request):
    if request.method == "POST":
        try:
            content = request.POST['content']
        except:
            content = ''
            
        if content:
            Blog.objects.create(
                content=content,
                user_id=request.user
            )

    return render(request, "index.html", {
        "title":"Home",
    })