from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

@login_required
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