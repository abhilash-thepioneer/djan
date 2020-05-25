from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
#from .models import Productnew,Contact,Orders
from math import ceil
# Create your views here.
import logging

logger=logging.getLogger(__name__)
def index(request):
	
	return render(request,'blog/index.html')