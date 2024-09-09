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
        max_length=50, verbose_name="город", help_text="Укажите город", **NULLABLE
    )

    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="аватар",
        help_text="Загрузите аватар",
        **NULLABLE,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payments")

    date_of_payment = models.DateTimeField(
        auto_now_add=False,
        **NULLABLE,
        verbose_name="Дата оплаты",
        help_text="Укажите дату оплаты",
    )

    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, **NULLABLE, related_name="payments"
    )

    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, **NULLABLE, related_name="payments"
    )

    payment_amount = models.IntegerField(verbose_name="Введите сумму оплаты")

    payment_method_is_cash = models.BooleanField(
        verbose_name="Способ оплаты - наличные",
        help_text="Укажите признак оплаты наличными",
    )

    class Meta:
        verbose_name = "платеж"
        verbose_name_plural = "платежи"

    def __str__(self):  # Измените на '__str__'
        # Корректное представление платежа
        return f"{self.user.email} ({self.course.name if self.course else self.lesson.name if self.lesson else 'Без курса/урока'} - {self.payment_amount})"
