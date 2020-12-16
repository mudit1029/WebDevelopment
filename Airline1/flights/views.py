from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
# Create your views here.
def index(request):
	return render(request, "flights/index.html", {
		"flights": Flight.objects.all()
		})

def info(request, flight_id):
	flight = Flight.objects.get(pk=flight_id)
	passengers = flight.passengers.all()
	return render(request, "flights/info.html", {
		"flight": flight,
		"passengers": passengers,
		"non_passenger": Passenger.objects.exclude(flights=flight).all()
		})	

def book(request, flight_id):
	if request.method == "POST":
		flight = Flight.objects.get(pk=flight_id)
		passenger = Passenger.objects.get(pk=int(request.POST["passengers"]))
		passenger.flights.add(flight)
		return HttpResponseRedirect(reverse("info", args=(flight.id,)))

