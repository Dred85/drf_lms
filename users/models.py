from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name="почта", help_text="Укажите почту"
    )

    phone = models.CharField(
        max_length=35, verbose_name="телефон", help_text="Укажите телефон", **NULLABLE
    )
    city = models.CharField(
        max_length=50, verbose_name="страна", help_text="Укажите город", **NULLABLE
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="аватар",
        help_text="Загрузите аватар",
        **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")

    date_of_payment = models.DateTimeField(
        auto_now_add=False,
        **NULLABLE,
        verbose_name="Дата оплаты",
        help_text="Укажите дату оплаты",
    )

    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, **NULLABLE, related_name="course"
    )
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, **NULLABLE, related_name="lesson"
    )

    payment_amount = models.IntegerField(verbose_name="введите сумму оплаты")

    payment_method_is_cash = models.BooleanField(
        verbose_name="способ оплаты - наличные",
        help_text="Укажите признак оплаты наличными",
    )

    class Meta:
        verbose_name = "платеж"
        verbose_name_plural = "платежи"

    def __str__(self):
        return f"{self.user} ({self.course if self.course else self.lesson} - {self.payment_amount})"