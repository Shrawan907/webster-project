from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'accounts/login.html', {'error': 'username or password is not correct!'})
    else:
        return render(request, 'accounts/login.html')

def signup(request):
    if request.method == 'POST':
        # User has info and wants an account
        if request.POST['password1'] == request.POST['password2']:
            try:    
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                # user nhi lika hua tha i hope ye problem nhi kre
                user = User.objects.create_user( request.POST['username'], password=request.POST['password1'] )
                auth.login(request,user)
                return redirect('home')
        else:
             return render(request, 'accounts/signup.html', {'error': 'Passwords must match'})

    else:
        # User wants to enter info
        return render(request, 'accounts/signup.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
