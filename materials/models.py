from django.db import models

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Название курса",
        help_text="Укажите название курса",
    )
    preview_image = models.ImageField(
        upload_to="materials_previews/",
        help_text="Загрузите превью (картинку) курса",
        **NULLABLE,
    )
    description = models.TextField(
        verbose_name="Описание курса", help_text="Сделайте описание курса", **NULLABLE
    )

    owner = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Владелец курса",
        help_text="Укажите владельца курса",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Название урока",
        help_text="Укажите название урока",
    )
    description = models.TextField(
        verbose_name="Описание курса", help_text="Сделайте описание урока", **NULLABLE
    )
    preview_image = models.ImageField(
        upload_to="lessons/photo",
        help_text="Загрузите превью (картинку) урока",
        **NULLABLE,
    )
    link_to_video = models.URLField(
        verbose_name="Ссылка на видео",
        max_length=200,
        help_text="Загрузите видео урока",
        **NULLABLE,
    )

    course = models.ForeignKey(
        Course,
        verbose_name="Курс",
        help_text="Выберите курс",
        on_delete=models.CASCADE,
        related_name="lessons",
        **NULLABLE,
    )

    owner = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Владелец урока",
        help_text="Укажите владельца урока",
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
