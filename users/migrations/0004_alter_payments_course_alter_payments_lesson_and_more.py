# Generated by Django 4.2 on 2024-09-04 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0001_initial"),
        ("users", "0003_alter_payments_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payments",
            name="course",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="payments",
                to="materials.course",
            ),
        ),
        migrations.AlterField(
            model_name="payments",
            name="lesson",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="payments",
                to="materials.lesson",
            ),
        ),
        migrations.AlterField(
            model_name="payments",
            name="payment_amount",
            field=models.IntegerField(verbose_name="Введите сумму оплаты"),
        ),
        migrations.AlterField(
            model_name="payments",
            name="payment_method_is_cash",
            field=models.BooleanField(
                help_text="Укажите признак оплаты наличными",
                verbose_name="Способ оплаты - наличные",
            ),
        ),
        migrations.AlterField(
            model_name="payments",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="payments",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="city",
            field=models.CharField(
                blank=True,
                help_text="Укажите город",
                max_length=50,
                null=True,
                verbose_name="город",
            ),
        ),
    ]
