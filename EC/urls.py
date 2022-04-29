from django.urls import  path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('app/', views.app, name='app'),
    path('log/', views.log, name='log'),
    path('save' , views.saveAudio , name='save'),
    path('detect' , views.getPrediction , name='detect'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)