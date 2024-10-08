# Generated by Django 5.0.6 on 2024-08-06 11:34

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0008_orderreview_review"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="review",
            name="flower",
        ),
        migrations.RemoveField(
            model_name="review",
            name="rating",
        ),
        migrations.AddField(
            model_name="review",
            name="text",
            field=models.TextField(default="", verbose_name="Отзыв"),
        ),
        migrations.AlterField(
            model_name="review",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reviews",
                to="catalog.order",
            ),
        ),
        migrations.CreateModel(
            name="FlowerRating",
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
                (
                    "rating",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ],
                        verbose_name="Рейтинг",
                    ),
                ),
                (
                    "flower",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ratings",
                        to="catalog.flower",
                    ),
                ),
                (
                    "review",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="flower_ratings",
                        to="catalog.review",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="OrderReview",
        ),
    ]
