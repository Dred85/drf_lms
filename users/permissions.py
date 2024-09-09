from rest_framework import permissions

class IsModer(permissions.BasePermission):
    message = 'Вы не являетесь модератором'

    def has_permission(self, request, view):
        """Делаем проверку на вхождение пользователя в группу"""
        return  request.user.groups.filter(name="moders1").exists()