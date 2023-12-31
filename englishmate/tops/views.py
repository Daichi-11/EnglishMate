from django.shortcuts import render, get_object_or_404
from flashcards.models import FlashCard

# Create your views here.
def home(request):
  flashcards = FlashCard.objects.all()
  return render(request, 'tops/home.html', {'flashcards': flashcards})
