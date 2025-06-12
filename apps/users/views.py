from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user =authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            print(user)
            login(request, user)
            return redirect('home')  
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'login.html')

def register_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password1')
        print(password)
        confirm_password=request.POST.get('password2')
        if password != confirm_password:
            return render(request, 'register.html', {'error': 'Passwords do not match'})
        else:
            user=User.objects.create_user(username=username, email=email, password=password)
            user.save()
            login(request, user)
            return redirect('home')
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('login')
