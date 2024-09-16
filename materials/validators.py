import re
from rest_framework.exceptions import ValidationError

# YOUTUBE_REGEX = r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.+$'
YOUTUBE_REGEX = "https://www.youtube.com/"

def validate_youtube_url(url):
    """Проверяет, что ссылка ведет на YouTube."""
    if not YOUTUBE_REGEX:
        raise ValidationError("Только ссылки на YouTube допустимы.")