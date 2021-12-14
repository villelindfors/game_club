
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
    # New game
    path('new_game/', views.new_game, name="new_game"),
    # New loan
    path('new_loan/<int:game_id>/', views.new_loan, name="new_loan"),
    # Edit loan
    path('edit_loan/<int:loan_id>/', views.edit_loan, name="edit_loan"),
]