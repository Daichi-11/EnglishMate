from django.db import models

# Create your models here.

class FlashCard(models.Model):
    image = models.ImageField(upload_to='flashcards/')
    definition = models.CharField(max_length=255)
    word = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.definition} - {self.word}"