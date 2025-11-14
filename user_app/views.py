from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as authlogin, logout as authlogout
from .models import Profile

# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        age = request.POST.get('age')

        if password1 != password2:
            return render(request, 'signup.html', {'error': 'Password do not match!'})
        
        if User.objects.filter(username = username).exists():
            return render(request, 'signup.html', {'error':'User already existed!'})
        
        user = User.objects.create_user(username = username, password = password1)
        user.save()

        Profile.objects.create(user = user,
                               name = name,
                               email = email,
                               phone = phone,
                               address = address,
                               age = age)
        return redirect('login')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            authlogin(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error':'Invalid username or password!'})
    return render(request, 'login.html')

def logout(request):
    authlogout(request)
    return redirect('index')

def view_users(request):
    user = Profile.objects.all()
    return render(request, 'view_users.html', {'userdata':user})
