
from django import forms
from .models import FlashCard, Deck

class FlashCardForm(forms.ModelForm):
    deck = forms.ModelChoiceField(queryset=Deck.objects.all(), empty_label=None)

    class Meta:
        model = FlashCard
        fields = ['image', 'definition', 'word']



class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = ['topic', 'description']
