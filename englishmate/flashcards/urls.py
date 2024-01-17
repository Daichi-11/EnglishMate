# flashcards/urls.py
from django.urls import path
from .views import deck_list, add_deck, flashcard_list, add_flashcard, play_pronunciation,dictionary

urlpatterns = [
    path('', deck_list, name='deck_list'),
    path('add_deck/', add_deck, name='add_deck'),
    path('<int:deck_id>/', flashcard_list, name='flashcard_list'),
    path('<int:deck_id>/add_flashcard/', add_flashcard, name='add_flashcard'),
    path('play_pronunciation/<int:flashcard_id>/', play_pronunciation, name='play_pronunciation'),
    path('dictionary/', dictionary, name='dictionary'),
]
