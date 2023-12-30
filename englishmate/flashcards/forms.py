
from django import forms
from .models import FlashCard

class FlashCardForm(forms.ModelForm):
    class Meta:
        model = FlashCard
        fields = ['front_image', 'front_definition', 'back_image', 'back_word']
