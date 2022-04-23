from django.urls import  path
from . import views

urlpatterns = [
    path('app/', views.app, name='app'),
    path('log/', views.log, name='log'),
<<<<<<< HEAD
    path('save' , views.saveAudio , name='save'),
    path('detect' , views.getPrediction , name='detect'),
=======
    
>>>>>>> 9735a40054aea9923a99f1ba17fcb6bd82531b7a
]
