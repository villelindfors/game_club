from django.shortcuts import redirect, render
from .models import Game, Loan
from .forms import GameForm, LoanForm

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
    loans = game.loan_set.order_by('-date_added')
    context = {'game':game, 'loans':loans}
    return render(request, 'game_clubs/game.html', context)

def new_game(request):
    """Add New Game"""
    if request.method != 'POST':
        #NO DATA SUBMITTED. CREATE A BLANK FORM
        form = GameForm()
    else:
        #POST DATA SUBMITTED. PROCESS DATA
        form = GameForm(data = request.POST)
        if form.is_valid():
            new_game = form.save(commit=False)
            new_game.owner = request.user
            new_game.save()
            return redirect('game_clubs:games') 

    context = {'form' : form}
    return render(request, 'game_clubs/new_game.html', context)

def new_loan(request, game_id):
    """Add new review for a book"""
    game = Game.objects.get(id=game_id)
    if request.method != 'POST':
        form = LoanForm()
    else:
        form = LoanForm(data=request.POST)
        if form.is_valid():
            new_loan = form.save(commit=False)
            new_loan.game = game
            new_loan.save()
            return redirect('game_clubs:game', game_id=game_id) 

    #Display blank or invalid form
    context = {'game' : game, 'form' : form}
    return render(request, 'game_clubs/new_loan.html', context)

def edit_loan(request, loan_id):
    loan = Loan.objects.get(id=loan_id)
    game = loan.game

    #Protecting edit loan page
    #if book.owner != request.user:
     #   raise Http404

    if request.method != 'POST':
        form = LoanForm(instance=loan)
    else:
        form = LoanForm(instance=loan, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('game_clubs:game', game_id = game.id)

    context = {'loan' : loan, 'game' : game, 'form' : form}
    return render(request, 'game_clubs/edit_loan.html', context)