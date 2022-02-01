from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def profile(request):
    #check if the user has logged in
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return HttpResponse('You are not logged in')
    return render(request, 'index.html')

# Views 
def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Account created successfully')
        login(request,user)
        return render(request, 'profile.html')
    else:
        return HttpResponse('entered else of regsiter')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username , password=password)

        if user is not None:
            login(request,user)
            messages.success(request, 'Login successful')
            return redirect( 'app')
        else:
             messages.error(request, 'Login Failed.')
             return render(request, 'index.html')
    else:
        messages.warning(request, 'Please enter username and password')
        return render(request, 'index.html')

def logout_view(request):
    logout(request)
    return render(request, 'index.html')

