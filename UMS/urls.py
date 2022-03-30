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
