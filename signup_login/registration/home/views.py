from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def main(request):
    return render(request, 'main.html')

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        
        if pass1 != pass2:
            return render(request, 'signup.html', {'error': 'Passwords do not match'})

        my_user = User.objects.create_user(uname, email, pass1)
        my_user.save()
        return redirect('login')
    return render(request, 'signup.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            auth_login(request, user)
            return redirect('main')
        else:
            return HttpResponse("Username or password is incorrect!!!")
        
    return render(request, 'login.html')

def user_logout(request):
    auth_logout(request)
    return redirect('login')
