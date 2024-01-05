from django.db import models
from django.contrib.auth.models import User


class FlashCard(models.Model):
    image = models.ImageField(upload_to='flashcards/')
    definition = models.CharField(max_length=255)
    word = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.definition} - {self.word}"


class Deck(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.topic