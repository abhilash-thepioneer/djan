from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib import auth
from .forms import RegistrationForm
from django.contrib import messages

def register(request):
	if request.method=="POST":
		form=RegistrationForm(data=request.POST)
		if form.is_valid():
			form.save()
			c=25
			messages.info(request,'your id is created success')

	form=RegistrationForm()
	return render(request,'account/register.html',{'form':form})

# Create your views here.
def login_view(request):
	if request.method=="POST":
		form=AuthenticationForm(data=request.POST)
		if form.is_valid():
			user=form.get_user()
			login(request,user)
			if 'next' in request.POST:
				return redirect(request.POST.get('next'))
			return redirect('/shop/')
	else:
		form=AuthenticationForm()
	return render(request,'account/login.html',{'form':form})

def logout_view(request):
	if request.method=="POST":
		auth.logout(request)
		return render(request,'account/logout.html')