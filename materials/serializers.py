from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson



class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    lesson_count = SerializerMethodField()  # Добавляем поле для количества уроков


    class Meta:
        model = Course
        fields = ['name', 'preview_image', 'description',
                  'lesson_count']

    def get_lesson_count(self, course):
        return Lesson.objects.filter(course=course).count()  # course это экземпляр класса Course


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"



