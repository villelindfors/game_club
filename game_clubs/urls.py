
from django.urls import path

from . import views

app_name = "game_clubs"

urlpatterns = [
    # Pages
    path('', views.index, name="index"),
    # Shows all games
    path('games/', views.games, name="games"),
    # Single game
    path('games/<int:game_id>/', views.game, name="game"),
]