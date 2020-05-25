from django.urls import path

# Create your models here.
from . import views
#urlspath=[]
urlpatterns = [
    path('',views.index,name="index"),
    	    path('about/',views.about,name="about"),
    	        path('contact/',views.contact,name="contact"),
    	            path('tracker/',views.tracker,name="tracker"),
    	                path('search/',views.search,name="search"),
    	                path('product/<int:myid>',views.productView,name="productView"),
    	                 path('checkout/',views.checkout,name="checkout"),
    	                 path('timepass/',views.tp,name="tp"),
                         path('items/',views.items,name='items'),
    	                 path("handlerequest/",views.handlerequest,name='handlerequest'),


    	                    	            ]
