from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate , login , logout
# Create your views here.

def index(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("sign_in"))
	return render(request, "user/index.html")

def sign_in(request):
	if request.method == 'POST':
		username = request.POST["username"]
		password = request.POST["password"]
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse("index"))
		else :
			return render(request, "user/login.html", {
				"message": "Invalid Credentials"
				})	
	return render(request, "user/login.html")

def sign_out(request):
	logout(request)
	return render(request, "user/login.html", {
		"message": "You Have Successfully Logged Out"
		})		