from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.flashcards, name='flashcards'), 
    path('create/', views.create_card_set, name='create_card_set'), 
    path('create_card/<int:card_set_id>/', views.create_card, name='create_card'), 
    path('delete/<int:card_set_id>/', views.delete_card_set, name='delete_card_set'), 
    path('delete_card/<int:card_id>/', views.delete_card, name='delete_card'), 
    path('edit/<int:card_set_id>/', views.edit_card_set, name='edit_card_set'),
    path('edit_card/<int:card_id>/', views.edit_card, name='edit_card'), 
    path('view/<int:card_set_id>/', views.view_card_set, name='view_card_set'), 
    path('dictionary/', views.dictionary, name='dictionary'), 
]
