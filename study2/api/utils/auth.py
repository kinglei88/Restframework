from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from api import models


class FirstAuthentication(BaseAuthentication):
    def authenticate(self,request):
        pass
    def authenticate_header(self,request):
        pass


class Authentication(BaseAuthentication):
    def authenticate(self,request):
        token = request._request.GET.get('token')
        token_obj = models.UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('用户认证失败2')

        # 在restframework内部赋值给request，以供后续操作使用
        return (token_obj.user,token_obj)

    def authenticate_header(self,request):
        pass


def abc():
    return 'Kobe'


def ghi():
    return 'Bryant'