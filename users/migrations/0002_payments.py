# Generated by Django 4.2 on 2024-09-04 18:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("materials", "0001_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payments",
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
                    "date_of_payment",
                    models.DateTimeField(
                        blank=True,
                        help_text="Укажите дату оплаты",
                        null=True,
                        verbose_name="Дата оплаты",
                    ),
                ),
                (
                    "payment_amount",
                    models.IntegerField(verbose_name="введите сумму оплаты"),
                ),
                (
                    "payment_method_is_cash",
                    models.BooleanField(
                        help_text="Укажите признак оплаты наличными",
                        verbose_name="способ оплаты - наличные",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="course",
                        to="materials.course",
                    ),
                ),
                (
                    "lesson",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lesson",
                        to="materials.lesson",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "платеж",
                "verbose_name_plural": "платежи",
            },
        ),
    ]
