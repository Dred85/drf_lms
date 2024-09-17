from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson, Subscription
from materials.validators import validate_youtube_url


class LessonSerializer(ModelSerializer):
    link_to_video = serializers.URLField(validators=[validate_youtube_url])

    class Meta:
        model = Lesson
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = Subscription
        fields = ["user_email"]


class CourseSerializer(ModelSerializer):
    lessons = LessonSerializer(
        many=True, read_only=True
    )  # Отобразить список уроков в курсе
    is_subscribed = SerializerMethodField()

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "preview_image",
            "description",
            "lessons",
            "owner",
            "is_subscribed",
        ]

    def get_is_subscribed(self, course):
        user = self.context["request"].user
        return Subscription.objects.filter(user=user, course=course).exists()


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
