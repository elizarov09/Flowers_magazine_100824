# Generated by Django 5.0.6 on 2024-08-06 08:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0005_remove_order_delivery_datetime_order_delivery_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("PENDING", "Ожидает обработки"),
                    ("PROCESSING", "В обработке"),
                    ("SHIPPING", "В доставке"),
                    ("COMPLETED", "Выполнен"),
                ],
                default="PENDING",
                max_length=20,
                verbose_name="Статус",
            ),
        ),
    ]
