
from django.shortcuts import render, get_object_or_404, redirect
from .models import FlashCard
from .forms import FlashCardForm

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
