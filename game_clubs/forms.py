from django import forms
from django.forms import fields, widgets

from .models import Game, Loan

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'maker']

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['my_loan']
        widgets = {'my_loan' : forms.Textarea(attrs={'cols': 80})}