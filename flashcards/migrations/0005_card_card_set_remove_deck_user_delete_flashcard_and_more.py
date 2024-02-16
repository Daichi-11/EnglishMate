# Generated by Django 5.0 on 2024-01-08 02:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("flashcards", "0004_deck"),
    ]

    operations = [
        migrations.CreateModel(
            name="Card",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("word", models.CharField(max_length=50)),
                ("definition", models.TextField(max_length=500)),
                ("sentences", models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="Card_Set",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("topic", models.CharField(max_length=50)),
                ("description", models.CharField(blank=True, max_length=300)),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="deck",
            name="user",
        ),
        migrations.DeleteModel(
            name="FlashCard",
        ),
        migrations.AddField(
            model_name="card",
            name="parent_card_set",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="flashcards.card_set"
            ),
        ),
        migrations.DeleteModel(
            name="Deck",
        ),
    ]