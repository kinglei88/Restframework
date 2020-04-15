from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from api import models
from api.models import UserInfo, UserToken
import hashlib
import time

def md5(username):

    ctime = str(time.time())
    m = hashlib.md5(bytes(username,encoding='utf-8'))
    m.update(bytes(ctime,encoding='utf-8'))
    return m.hexdigest()

class AuthView(APIView):

    def post(self,request):

        ret = {'code':1000,'msg':'xxxx'}
        try:
            user = request._request.POST.get('username')
            pwd = request._request.POST.get('password')
            obj = UserInfo.objects.filter(username=user, password=pwd).first()

            if not obj:
                ret['code'] = 1001
                ret['msg'] = '用户名或密码错误'

                return JsonResponse(ret)

            token = md5(user)
            models.UserToken.objects.update_or_create(user=obj,defaults={'token':token})
            ret['token'] = token

            # todo 直接更新
            # UserToken.objects.filter(user_id=obj.id).update(token=token)

            # todo 复杂写法
            # obj2 = UserToken.objects.filter(user_id=2).first()
            # if obj2:
            #     obj2.token = 'sssss'
            #     obj2.save()
            # else:
            #     obj2 = UserToken()
            #     obj2.token = '12312312313213'
            #     obj2.user_id = obj.id
            #     obj2.save()

        except:
            ret['code'] = 1002
            ret['msg'] = '请求异常'









        return JsonResponse(ret)