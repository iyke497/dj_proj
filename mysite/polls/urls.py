from django.urls import path

from . import views


#Path function is passed 4 arguments 2 required {route and view} and 2 optional kwargs and name
urlpatterns = [
	path("", views.index, name="index"),
]