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
    path('sendmsg/', views.sendFeedBacks, name='sendmsg'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
