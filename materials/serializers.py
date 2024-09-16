from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson
from materials.validators import validate_youtube_url


class LessonSerializer(ModelSerializer):
    link_to_video = serializers.URLField(validators=[validate_youtube_url])
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    lessons = LessonSerializer(
        many=True, read_only=True
    )  # Отобразить список уроков в курсе

    class Meta:
        model = Course
        fields = ["id", "name", "preview_image", "description", "lessons", "owner"]


class CourseDetailSerializer(ModelSerializer):
    lesson_count = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "preview_image",
            "description",
            "lesson_count",
            "lessons",
            "owner",
        ]

    @staticmethod
    def get_lesson_count(course):
        return course.lessons.count()
