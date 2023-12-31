
from django import forms
from .models import FlashCard

class FlashCardForm(forms.ModelForm):
    class Meta:
        model = FlashCard
        fields = ['image', 'definition', 'word']
