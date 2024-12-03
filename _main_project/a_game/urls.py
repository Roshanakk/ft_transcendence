from django.urls import path
from . import views

urlpatterns = [
	path("create_game/", views.create_game_session, name="create_game"),
	path("join_game/", views.join_game_session, name="join_game"),
]