from django.urls import  path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('register', views.register, name="register"),
    path('login', views.login_view),
    path('logout', views.logout_view),
]
