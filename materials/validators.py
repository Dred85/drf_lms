import re

from rest_framework.exceptions import ValidationError

# YOUTUBE_REGEX = r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.+$'
YOUTUBE_REGEX = "youtube.com"


def validate_youtube_url(url):
    """Проверяет, что ссылка ведет на YouTube."""
    if YOUTUBE_REGEX not in url:
        raise ValidationError(
            "Запрещается использовать ссылки на сторонние ресурсы, кроме youtube.com"
        )
