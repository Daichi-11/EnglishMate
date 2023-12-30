from django.db import models

# Create your models here.

class FlashCard(models.Model):
    front_image = models.ImageField(upload_to='flashcards/')
    front_definition = models.CharField(max_length=255)
    back_image = models.ImageField(upload_to='flashcards/')
    back_word = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.front_definition} - {self.back_word}"