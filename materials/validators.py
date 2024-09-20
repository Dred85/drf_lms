from rest_framework.exceptions import ValidationError

YOUTUBE_REGEX = "youtube.com"


def validate_youtube_url(url):
    """Проверяет, что ссылка ведет на YouTube."""
    if YOUTUBE_REGEX not in url:
        raise ValidationError(
            "Запрещается использовать ссылки на сторонние ресурсы, кроме youtube.com"
        )
