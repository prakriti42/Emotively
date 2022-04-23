<<<<<<< HEAD
from django.urls import  path , include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('login', views.login_view),
    path('register/', views.register , name='register'),
    path('logout', views.logout_view),
    path('accounts/', include('allauth.urls')),
    path('update/', views.profile_update, name='update'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
from django.urls import  path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('base', views.base , name = 'base'),
    path('profile/', views.profile, name='profile'),
    path('register', views.register, name="register"),
    path('login', views.login_view),
    path('logout', views.logout_view),
    path('message', views.message),
]
>>>>>>> 9735a40054aea9923a99f1ba17fcb6bd82531b7a
