from django.shortcuts import render
from .models import Game, Loan

# Create your views here.
def index(request):
    return render(request, "game_clubs/index.html")

def games(request):
    """Show all games"""
    games = Game.objects.order_by('date_added')
    context = {'games' : games}
    return render(request, 'game_clubs/games.html', context)

def game(request, game_id):
    """Show a single game and its review and loans"""
    game = Game.objects.get(id=game_id)
    reviews = game.review_set.order_by('-date_added')
    context = {'game':game, 'reviews':reviews}
    return render(request, 'game_clubs/game.html', context)