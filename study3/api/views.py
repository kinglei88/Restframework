from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView



class User(APIView):
    def get(self,request,*args,**kwargs):
        self.dispatch()

        # todo 获取版本
        print(request.version)
        # todo 获取处理版本的对象
        print(request.versioning_scheme)
        return HttpResponse('hello world')