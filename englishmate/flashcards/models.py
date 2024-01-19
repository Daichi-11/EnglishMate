# flashcards/models.py
from django.db import models

class Deck(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='deck_images/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class Flashcard(models.Model):
    word = models.CharField(max_length=100)
    definition = models.TextField()
    pronunciation = models.FileField(upload_to='pronunciations/', null=True, blank=True)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.deck.title} - {self.word}"
