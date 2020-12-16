from . import views
from django.urls import path

urlpatterns = [
	path('', views.index , name='index'),
	path('counter/', views.counter, name="counter"),
	path('game/', views.game, name='game'),
]