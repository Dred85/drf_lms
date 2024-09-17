from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson, Subscription
from users.models import User


class LessonTestCase(APITestCase):
    """Тесты уроков"""

    def setUp(self) -> None:
        self.user = User.objects.create(email="test@test.ru")
        self.course = Course.objects.create(name="test", description="test")
        self.lesson = Lesson.objects.create(
            name="test", description="test", course=self.course, owner=self.user
        )
        self.client.force_authenticate(
            user=self.user)  # "принудительно" указать клиенту, что определенный пользователь аутентифицирован для всех запросов

    def test_retrieve_lesson(self):
        """Тестирование вывода одного урока"""
        url = reverse("materials:lessons_retrieve", args=[self.lesson.pk])
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.lesson.name)

    def test_create_lesson_invalid_url(self):
        """Тестирование валидации создания урока с недействительной ссылкой и проверка сообщения об ошибке"""
        url = reverse("materials:lessons_create")
        data = {
            "name": "new test valid",
            "description": "new test valid",
            "link_to_video": "https://myvideo.com/lesson",  # Не YouTube ссылка
        }

        response = self.client.post(url, data=data)

        # Ожидаем статус ошибки валидации (400 Bad Request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Проверяем, что урок не был создан
        # self.assertEqual(Lesson.objects.count(), 0)

        # Проверяем, что в ответе содержится конкретное сообщение об ошибке
        self.assertIn("Запрещается использовать ссылки на сторонние ресурсы, кроме youtube.com",
                      response.data['link_to_video'])

    def test_create_lesson(self):
        """Тестирование создания урока"""
        url = reverse("materials:lessons_create")
        data = {
            "name": "new test",
            "description": "new test",
            "link_to_video": "https://youtube.com/lesson",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(2, Lesson.objects.all().count())

    def test_update_lesson(self):
        """Тестирование редактирования урока"""
        url = reverse("materials:lessons_update", args=[self.lesson.pk])
        data = {"name": "update test"}
        response = self.client.patch(url, data=data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "update test")

    def test_destroy_lesson(self):
        """Тестирование удаления урока"""
        url = reverse("materials:lessons_delete", args=[self.lesson.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(0, Lesson.objects.all().count())

    def test_list_lesson(self, null=None):
        """Тестирование вывода списка уроков"""
        url = reverse("materials:lessons_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = {
            "count": 1,
            "next": null,
            "previous": null,
            "results": [
                {
                    "id": self.lesson.pk,
                    "link_to_video": self.lesson.link_to_video,
                    "name": self.lesson.name,
                    "preview_image": null,  # Changed to 'preview_image'
                    "description": self.lesson.description,
                    "course": self.lesson.course.pk,
                    "owner": self.lesson.owner.pk,
                }
            ],
        }
        data = response.json()
        self.assertEqual(data, result)


class SubscriptionTestCase(APITestCase):
    """Тестирование создания и удаления подписок на курсы"""

    def setUp(self) -> None:
        self.user = User.objects.create(email="test@test.ru")

        self.course_1 = Course.objects.create(
            name="test", description="test", owner=self.user
        )
        self.course_2 = Course.objects.create(
            name="test2", description="test2", owner=self.user
        )
        self.subscription = Subscription.objects.create(
            user=self.user, course=self.course_1
        )
        self.client.force_authenticate(user=self.user)

    def test_post_subscription(self):
        """Тестирование подписки на курс"""
        url = reverse("materials:subscribe")
        data_1 = {"user": self.user.pk, "course": self.course_1.pk}
        data_2 = {"user": self.user.pk, "course": self.course_2.pk}

        response_1 = self.client.post(url, data_1)
        self.assertEqual(response_1.status_code, status.HTTP_200_OK)
        self.assertEqual(0, Subscription.objects.all().count())
        response_2 = self.client.post(url, data_2)
        self.assertEqual(response_2.status_code, status.HTTP_200_OK)
        self.assertEqual(1, Subscription.objects.all().count())


class CourseTestCase(APITestCase):
    """Тестирование курсов"""

    def setUp(self) -> None:
        self.user = User.objects.create(email="test@test.ru")
        self.course = Course.objects.create(name="test", description="test", owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_create_course(self):
        """Тестирование создания курса"""
        url = reverse("materials:course-list")
        data = {
            "name": "new_course",
            "description": "new_course",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(2, Course.objects.all().count())

    def test_update_course(self):
        """Тестирование редактирования курса"""
        url = reverse("materials:course-detail", args=[self.course.pk])
        data = {"name": "update test"}
        response = self.client.patch(url, data=data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "update test")

    def test_destroy_lesson(self):
        """Тестирование удаления курса"""
        url = reverse("materials:course-detail", args=[self.course.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(0, Lesson.objects.all().count())
