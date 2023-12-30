# flashcards/urls.py
from django.urls import path
from .views import flashcard_list, flashcard_detail, flashcard_create, flashcard_edit, flashcard_delete

urlpatterns = [
    path('', flashcard_list, name='flashcard_list'),
    path('<int:pk>/', flashcard_detail, name='flashcard_detail'),
    path('create/', flashcard_create, name='flashcard_create'),
    path('<int:pk>/edit/', flashcard_edit, name='flashcard_edit'),
    path('<int:pk>/delete/', flashcard_delete, name='flashcard_delete'),
]
