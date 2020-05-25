from django.shortcuts import render

# Create your views here.
from django.conf.urls import url,include
from django.urls import path
from django.contrib import admin
from account import views
from django.contrib.auth import views as auth_views
app_name='account'

urlpatterns = [

 #path('',views.index,name='index'),
 path('register/',views.register,name='register'),
path('login/',views.login_view,name='login_view'), 
  path('admin/',admin.site.urls),
  path('',include("django.contrib.auth.urls")),
  path('logout/',views.logout_view,name='logout_view'), 

  ]