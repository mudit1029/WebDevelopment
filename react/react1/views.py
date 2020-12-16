from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, "react1/index.html")

def counter(request):
	return render(request, "react1/counter.html")	

def game(request):
	return render(request, "react1/game.html")	