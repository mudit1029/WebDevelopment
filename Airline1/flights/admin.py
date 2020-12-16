from django.contrib import admin
from .models import *
# Register your models here.
class flight_display(admin.ModelAdmin):
	list_display = ("id" , "origin" , "destination" , "duration")

class passenger_display(admin.ModelAdmin):	
	filter_horizontal = ("flights", )

admin.site.register(Airport)
admin.site.register(Flight, flight_display)
admin.site.register(Passenger, passenger_display)