from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

class addtask(forms.Form):
	new = forms.CharField(label = "Add Task")

# Create your views here.
def index(request):
	if "tasks" not in request.session:
		request.session["tasks"] = []
	return render(request, 'tasks/index.html', {
		"tasks": request.session["tasks"]
		})

def add(request):
	if request.method == "POST":
		data = addtask(request.POST)
		if data.is_valid():
			task = data.cleaned_data["new"]
			request.session["tasks"] += [task]
			return HttpResponseRedirect(reverse("tasks:index"))
		else :
			return render(request, "tasks/add.html", {
				"task": data
				})	

	return render(request, "tasks/add.html", {
		"task": addtask
		})	
