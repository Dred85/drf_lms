from rest_framework import permissions


class IsModer(permissions.BasePermission):
    """Проверяет, является ли пользователь модератором"""

    message = "Вы не являетесь модератором"

    def has_permission(self, request, view):
        """Делаем проверку на вхождение пользователя в группу"""
        return request.user.groups.filter(name="moders").exists()


class IsOwner(permissions.BasePermission):
    """
    Разрешение на уровне объекта, позволяющее редактировать его только владельцам объекта
    """

    def has_object_permission(self, request, view, obj):
        # Разрешения на чтение разрешены для любого запроса,
        # поэтому мы всегда разрешаем запросы GET, HEAD или OPTIONS.
        if obj.owner == request.user:
            return True
        return False
