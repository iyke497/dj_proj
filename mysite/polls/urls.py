from django.urls import path

from . import views

app_name = "polls"
#Path function is passed 4 arguments 2 required {route and view} and 2 optional kwargs and name
urlpatterns = [
	path("", views.index, name="index"),
	path("<int:question_id>/", views.detail, name="detail"),
	path("<int:question_id>/results/", views.results, name="results"),
	path("<int:question_id>/vote/", views.vote, name="vote"),
]