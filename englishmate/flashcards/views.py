from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.conf import settings
from django.templatetags.static import static
from django.core.exceptions import ImproperlyConfigured
import os

from .models import Deck, Flashcard
from .forms import DeckForm, FlashcardForm
from PyDictionary import PyDictionary


def play_pronunciation(request, flashcard_id):
    flashcard = get_object_or_404(Flashcard, id=flashcard_id)
    pronunciation_path = flashcard.pronunciation.path

    if not os.path.isfile(pronunciation_path):
        raise ImproperlyConfigured("Pronunciation file not found.")

    with open(pronunciation_path, 'rb') as pronunciation_file:
        response = HttpResponse(pronunciation_file.read(), content_type='audio/mpeg')
        response['Content-Disposition'] = f'inline; filename="{flashcard.word}.mp3"'
        return response
    
def deck_list(request):
    decks = Deck.objects.all()
    return render(request, 'flashcards/deck_list.html', {'decks': decks})

def add_deck(request):
    if request.method == 'POST':
        form = DeckForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('deck_list')
    else:
        form = DeckForm()
    return render(request, 'flashcards/add_deck.html', {'form': form})

def flashcard_list(request, deck_id):
    deck = Deck.objects.get(id=deck_id)
    flashcards = Flashcard.objects.filter(deck=deck)
    return render(request, 'flashcards/flashcard_list.html', {'deck': deck, 'flashcards': flashcards})

def add_flashcard(request, deck_id):
    deck = Deck.objects.get(id=deck_id)
    if request.method == 'POST':
        form = FlashcardForm(request.POST, request.FILES)
        if form.is_valid():
            flashcard = form.save(commit=False)
            flashcard.deck = deck
            flashcard.save()
            return redirect('flashcard_list', deck_id=deck.id)
    else:
        form = FlashcardForm()
    return render(request, 'flashcards/add_flashcard.html', {'deck': deck, 'form': form})


def dictionary(request):
    try:
        if request.method == 'GET':
            word_searched = request.GET.get('word_searched')
            dictionary = PyDictionary()
            word_def = dictionary.meaning(word_searched)
            word_def = list(word_def.values())[0][0]
    except:
        word_def = 'この言葉は辞書にありません/英単語を検索してください'

    context = {'word_searched': word_searched, 'word_def': word_def}
    return render(request, 'flashcards/dictionary.html', context)