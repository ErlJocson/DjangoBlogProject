from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from post.models import Blog

def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('home')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user_to_login = authenticate(
            username=username,
            password=password
        )

        try:
            login(request, user_to_login)
            messages.success(request, f'Welcome back {username}')
            return redirect('home')
        except:
            messages.warning(request, 'There was an error!')

    return render(request, 'login.html', {
        "title":"Login"
    })

def register_view(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            try:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=password,
                )
                user.save()
                login(request, user)
                return redirect('home')
            except:
                messages.warning(request, 'There was an error!')
        else:
            messages.warning(request, 'Password is not a match!')

    return render(request, 'register.html', {
        "title":"Register"
    })

def logout_view(request):
    try:
        logout(request)
        messages.success(request, 'Logout success')
    except:
        messages.warning(request, 'There was an error!')
        
    return redirect('login')

@login_required
def profile_view(request):
    current_user = User.objects.get(id=request.user.id)
    user_blog = Blog.objects.filter(user_id=request.user).order_by('-date')
    return render(request, "profile.html", {
        'title':'Profile',
        'blogs':user_blog,
        'current_user':current_user
    })