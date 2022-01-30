from django.shortcuts import render
from . import views

# Create your views here.
def app(request):
    return render(request, 'app.html')

