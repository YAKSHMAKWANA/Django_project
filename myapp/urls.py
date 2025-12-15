from django.urls import path
from.views import index,about,login,contact,tour,destination,blog,register,logout


urlpatterns = [
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('login/',login,name='login'),
    path('contact/',contact,name='contact'),
    path('register/',register,name='register'),
    path('tour/',tour,name='tour'),
    path('destination/',destination,name='destination'),
    path('blog/',blog,name='blog'),
    path('logout/',logout,name='logout'),
    path('index/',index,name='index.html'),
]
