from django.urls import path

# Create your models here.
from . import  views
#urlspath=[]
urlpatterns = [
path('',views.index,name='index'),]
