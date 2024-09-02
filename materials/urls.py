from django.urls import path
from rest_framework.routers import SimpleRouter

from materials.views import (
    CourseViewSet,
    LessonCreateApiView,
    LessonUpdateAPIView,
    LessonDestroyAPIView,
    LessonListApiView,
    LessonRetrieveAPIView,
)
from materials.apps import MaterialsConfig


app_name = MaterialsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("lessons/", LessonListApiView.as_view(), name="lessons_list"),
    path(
        "lessons/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lessons_retrieve"
    ),  # retrieve это PUTCH
    path("lessons/create/", LessonCreateApiView.as_view(), name="lessons_create"),
    path(
        "lessons/<int:pk>/update/", LessonUpdateAPIView.as_view(), name="lessons_update"
    ),  # update это PUT
    path(
        "lessons/<int:pk>/delete/",
        LessonDestroyAPIView.as_view(),
        name="lessons_delete",
    ),
]

urlpatterns += router.urls
