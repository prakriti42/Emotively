from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Profile , Messages
from .forms import ProfileForm
from datetime import datetime
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    return render(request, 'index.html')

def profile(request):
    #check if the user has logged in
    if request.user.is_authenticated:
        data = Profile.objects.get(user=request.user)
        return render(request, 'profile.html' , {'data' : data})
    else:
        messages.warning(request, 'Log In Required')           
        return render(request, 'index.html')


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
        Profile(user=user, email=email).save()
        messages.success(request, 'Account created successfully')
      #  messages.success(request, 'Sign Up successful. Time to complete your profile.')
        return HttpResponseRedirect("/")
    else:
        messages.error(request, 'Please fill in all the fields correctly.')
        return HttpResponse('entered else of regsiter')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username , password=password)

        if user is not None:
            login(request,user)
            messages.success(request, 'Login successful.')
            return redirect(profile)
        else:
             messages.info(request, 'User not found.')           
             return render(request, 'index.html')
    else:
        messages.warning(request, 'Please enter username and password')
        return render(request, 'index.html')


def logout_view(request):
    logout(request)
    messages.success(request, "Logged Out Sucessfully")
    return render(request, 'index.html')


def profile_update(request):

    if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            if request.FILES['dp'] is not None or '': 
                dp = request.FILES['dp']
                fs = FileSystemStorage()
                filename = fs.save(dp.name, dp)
                uploaded_file_url = fs.url(filename)
                print("uploaded file url",uploaded_file_url)
                Profile.objects.filter(pk=request.user).update(firstname=first_name, lastname=last_name, dp = dp, email=email)
                messages.success(request, 'Profile Updated Successfully')
            else :
                Profile.objects.filter(pk=request.user).update(firstname=first_name, lastname=last_name, email=email)
                messages.success(request, 'Profile Updated Successfully')
            data = Profile.objects.filter(user = request.user)
    return redirect(to='/profile' , data = data)


def sendFeedBacks(request):
    if request.method == 'POST':
        message = request.POST['message']
        feedback = Messages(message=message)
        email_body = "Message: "+message +"\n" + "At: "+ str(datetime.now())
        feedback.save()
        # send_mail("Emotively", email_body , "Anonymous", ["regmi.prakriti24@gmail.com"])
        messages.success(request, 'Concerns and Queries Sent To Admin  Successfully')
        
        # messages.error(request, 'Failed to send Feedback Via Email')
        return redirect('/')
   
    return redirect(to='/')
