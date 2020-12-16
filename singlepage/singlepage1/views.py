from django.shortcuts import render
from django.http import HttpResponse , Http404

texts = ["This Is The First Page", "This Is The Second Page", "This Is The Third Page" ]
# Create your views here.
def index(request):
	return render(request, "singlepage1/index.html")

def section(request, num):
	if 1<=num<=3 :
		return HttpResponse(texts[num - 1])
	else :
		raise Http404("No Such Section")	
