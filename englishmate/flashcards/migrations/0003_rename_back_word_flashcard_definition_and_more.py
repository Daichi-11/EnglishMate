# Generated by Django 5.0 on 2023-12-31 01:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("flashcards", "0002_remove_flashcard_back_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="flashcard",
            old_name="back_word",
            new_name="definition",
        ),
        migrations.RenameField(
            model_name="flashcard",
            old_name="front_image",
            new_name="image",
        ),
        migrations.RenameField(
            model_name="flashcard",
            old_name="front_definition",
            new_name="word",
        ),
    ]