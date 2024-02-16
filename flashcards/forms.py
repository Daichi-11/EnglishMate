# flashcards/forms.py
from django import forms
from .models import Deck, Flashcard

class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = ['title', 'image', 'description']

class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['word', 'definition', 'pronunciation', 'deck']
