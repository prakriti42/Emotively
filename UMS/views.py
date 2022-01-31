from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User, auth


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
        return render(request, 'index.html')
    else:
        return HttpResponse('entered else of regsiter')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username , password=password)

        if user is not None:
            login(request,user)
            return render(request, 'app.html')
    else:
        return HttpResponse('entered else of login')

def logout_view(request):
    logout(request)
    return render(request, 'index.html')

