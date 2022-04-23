from django.shortcuts import render , redirect
<<<<<<< HEAD
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile
from .forms import ProfileForm

=======
from django.http import HttpResponse
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User, auth
from django.contrib import messages


def base(request):
    return render(request, 'try.html')
>>>>>>> 9735a40054aea9923a99f1ba17fcb6bd82531b7a
# Create your views here.
def index(request):
    return render(request, 'index.html')

def profile(request):
    #check if the user has logged in
    if request.user.is_authenticated:
<<<<<<< HEAD
        data = Profile.objects.get(user=request.user)
        return render(request, 'profile.html' , {'data' : data})
    else:
        messages.warning(request, 'Log In Required')           
        return render(request, 'index.html')


    return render(request, 'index.html')

# Views 

def register(request):
=======
        return render(request, 'profile.html')
    else:
        return HttpResponse('You are not logged in')
    return render(request, 'index.html')

# Views 
def register(request):

>>>>>>> 9735a40054aea9923a99f1ba17fcb6bd82531b7a
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
<<<<<<< HEAD
        Profile(user=user, email=email).save()
        messages.success(request, 'Account created successfully')
      #  messages.success(request, 'Sign Up successful. Time to complete your profile.')
        return HttpResponseRedirect("/")
    else:
        messages.error(request, 'Please fill in all the fields correctly.')
=======
        messages.success(request, 'Account created successfully')
        login(request,user)
        return render(request, 'profile.html')
    else:
>>>>>>> 9735a40054aea9923a99f1ba17fcb6bd82531b7a
        return HttpResponse('entered else of regsiter')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username , password=password)

        if user is not None:
            login(request,user)
<<<<<<< HEAD
            messages.success(request, 'Login successful.')
            return redirect(profile)
        else:
             messages.info(request, 'User not found.')           
=======
            messages.success(request, 'Login successful')
            return redirect( 'app')
        else:
             messages.error(request, 'Login Failed.')
>>>>>>> 9735a40054aea9923a99f1ba17fcb6bd82531b7a
             return render(request, 'index.html')
    else:
        messages.warning(request, 'Please enter username and password')
        return render(request, 'index.html')

<<<<<<< HEAD

def logout_view(request):
    logout(request)
    messages.success(request, "Logged Out Sucessfully")
    return render(request, 'index.html')


def profile_update(request):

    if request.method == 'GET' and 'q' in request.GET:
        if query is None:
            return HttpResponse('No results found')
        else:
            first_name = request.GET['first_name']
            last_name = request.GET['last_name']
            email = request.GET['email']
            print("The first name is "+first_name)
            # user = request.user
            request.user.first_name = first_name
            request.user.last_name = last_name
            request.user.email = email
            request.user.save()
            messages.success(request, 'Profile Updated Successfully')
            Profile(user= request.user,firstname=first_name, lastname=last_name, email=email).save()
            request.user.save()
            messages.success(request, 'Profile Updated Successfully')
            data = Profile.objects.get(user=request.user)
            return render(request, "profile.html", {'data' : data})
    else : 
        messages.INFO(request, 'Please fill in all the fields correctly.')
        return render(request, "profile.html",{'data' : data})
    messages.error(request, "Failed to Update Profile Details.")
    return render(request, "profile.html", {'data' : data})
=======
def logout_view(request):
    logout(request)
    return render(request, 'index.html')

def message(request):
    return render(request, "message.html")
>>>>>>> 9735a40054aea9923a99f1ba17fcb6bd82531b7a
