
from django.contrib import admin
from .models import Deck, Flashcard

class FlashcardInline(admin.TabularInline):
    model = Flashcard
    extra = 1

class DeckAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    inlines = [FlashcardInline]

class FlashcardAdmin(admin.ModelAdmin):
    list_display = ('word', 'definition', 'deck',)
    list_filter = ('deck',)

admin.site.register(Deck, DeckAdmin)
admin.site.register(Flashcard, FlashcardAdmin)
