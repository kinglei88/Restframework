from rest_framework.permissions import BasePermission

class SvipMyPermission(BasePermission):
    def has_permission(self,request,view):
        user_type = request.user.user_type

        if user_type != 3:
            return False
        return True


class MyPermission(BasePermission):
    def has_permission(self,request,view):
        user_type = request.user.user_type

        if user_type == 3:
            return False
        return True