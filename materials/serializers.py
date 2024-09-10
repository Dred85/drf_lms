from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class LessonSerializer(ModelSerializer):
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
