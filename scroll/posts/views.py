from django.shortcuts import render
import time
from django.http import JsonResponse
# Create your views here.
def index(request):
	return render(request, "posts/index.html")

def posts(request):
	
	# Get Start And End Points	
	start = int(request.GET.get("start") or 0)
	end = int(request.GET.get("end") or (start + 9))

	# Generate List Of Posts
	data = []
	for i in range(start , end + 1):
		data.append(f"Post #{i}")

	# Artificially Delay Speed Of Response	
	time.sleep(1)

	#Return List Of Posts
	return JsonResponse({
		"posts": data
		})