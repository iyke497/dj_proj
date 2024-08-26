from django.urls import path

from . import views

app_name = "polls"
#Path function is passed 4 arguments 2 required {route and view} and 2 optional kwargs and name
urlpatterns = [
	path("", views.IndexView.as_view(), name="index"),
	path("<int:pk>/", views.DetailView.as_view(), name="detail"),
	path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
	path("<int:question_id>/vote/", views.vote, name="vote"),
]