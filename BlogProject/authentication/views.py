from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user_to_login = authenticate(
            username=username,
            password=password
        )

        try:
            login(request, user_to_login)
            return redirect('index')
        except:
            messages.warning(request, 'There was an error!')

    return render(request, 'login.html', {
        "title":"Login"
    })

def register_view(request):
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
            except:
                messages.warning(request, 'There was an error!')
        else:
            messages.warning(request, 'Password is not a match!')

    return render(request, 'register.html', {
        "title":"Register"
    })