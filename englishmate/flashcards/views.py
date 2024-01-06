
from django.shortcuts import render, get_object_or_404, redirect
from .models import FlashCard, Deck
from .forms import FlashCardForm, DeckForm
from PyDictionary import PyDictionary
from django.contrib.auth.decorators import login_required

@login_required
def deck_list(request):
    decks = Deck.objects.filter(user=request.user)
    return render(request, 'decks/deck_list.html', {'decks': decks})

@login_required
def add_deck(request):
    if request.method == 'POST':
        form = DeckForm(request.POST)
        if form.is_valid():
            deck = form.save(commit=False)
            deck.user = request.user
            deck.save()
            return redirect('deck_list')
    else:
        form = DeckForm()
    return render(request, 'decks/add_deck.html', {'form': form})

def flashcard_list(request):
    flashcards = FlashCard.objects.all()
    return render(request, 'flashcards/flashcard_list.html', {'flashcards': flashcards})

def flashcard_detail(request, pk):
    flashcard = get_object_or_404(FlashCard, pk=pk)
    return render(request, 'flashcards/flashcard_detail.html', {'flashcard': flashcard})

def flashcard_create(request):
    if request.method == 'POST':
        form = FlashCardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('flashcard_list')
    else:
        form = FlashCardForm()

    return render(request, 'flashcards/flashcard_form.html', {'form': form})

def flashcard_edit(request, pk):
    flashcard = get_object_or_404(FlashCard, pk=pk)
    if request.method == 'POST':
        form = FlashCardForm(request.POST, request.FILES, instance=flashcard)
        if form.is_valid():
            form.save()
            return redirect('flashcard_list')
    else:
        form = FlashCardForm(instance=flashcard)

    return render(request, 'flashcards/flashcard_form.html', {'form': form})

def flashcard_delete(request, pk):
    flashcard = get_object_or_404(FlashCard, pk=pk)
    if request.method == 'POST':
        flashcard.delete()
        return redirect('flashcard_list')

    return render(request, 'flashcards/flashcard_confirm_delete.html', {'flashcard': flashcard})



def dictionary(request):
    word_searched = request.GET.get('word_searched', '')
    word_def = None

    try:
        if word_searched:
            dictionary = PyDictionary()
            meanings = dictionary.meaning(word_searched)

            if meanings:
                word_def = meanings[list(meanings.keys())[0]][0]
            else:
                word_def = 'Meaning not found for the word'
    except Exception as e:
        word_def = f"An error occurred: {str(e)}"

    context = {'word_searched': word_searched, 'word_def': word_def}
    return render(request, 'flashcards/dictionary.html', context)