from django.urls import  path
from . import views

urlpatterns = [
    path('app/', views.app, name='app'),
    path('log/', views.log, name='log'),
    
]
