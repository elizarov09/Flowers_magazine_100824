# Generated by Django 5.0.6 on 2024-08-05 10:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0003_order"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="delivery_date",
        ),
        migrations.RemoveField(
            model_name="order",
            name="delivery_time",
        ),
        migrations.AddField(
            model_name="order",
            name="comment",
            field=models.TextField(blank=True, null=True, verbose_name="Комментарий"),
        ),
        migrations.AddField(
            model_name="order",
            name="delivery_datetime",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
