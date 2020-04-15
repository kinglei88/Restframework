import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt, csrf_protect


# @csrf_exempt
# @csrf_protect
# def index(request):
#
#     user_list = ['hello','world']
#
#
#     return HttpResponse(json.dumps(user_list))
#
#
# class MyBaseView(object):
#
#     # todo 可以起到装饰器的作用
#     @method_decorator(csrf_exempt)
#     def dispatch(self,request,*args,**kwargs):
#
#         print('before')
#         ret = super(MyBaseView,self).dispatch(request,*args,**kwargs)
#         print('after')
#         return ret
#
#
# class StudentsView(MyBaseView,View):
#
#     @method_decorator(csrf_protect)
#     def dispatch(self,request,*args,**kwargs):
#         ret = super(StudentsView, self).dispatch(request,*args,**kwargs)
#         return ret
#
#
#     def get(self,request,*args,**kwargs):
#         return HttpResponse('GET')
#
#
#     def post(self,request,*args,**kwargs):
#         return HttpResponse('POST')
#
#     def put(self,request,*args,**kwargs):
#         return HttpResponse('PUT')
#
#     def delete(self,request,*args,**kwargs):
#         return HttpResponse('DELETE')
#
#
# class OrderView(View):
#
#     def get(self,request,*args,**kwargs):
#
#         ret = {
#             'code':1000,
#             'msg':'xxxx'
#         }
#
#         return HttpResponse(json.dumps(ret),status=201)
#
#     def post(self,request,*args,**kwargs):
#         return HttpResponse('创建订单')
#
#     def put(self,request,*args,**kwargs):
#         return HttpResponse('修改订单')
#
#     def delete(self,request,*args,**kwargs):
#         return HttpResponse('删除订单')

################################################
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework import exceptions

class MyAuthentication(object):
    def authenticate(self,request):
        token = request._request.GET.get('token')
        if not token:
            raise exceptions.AuthenticationFailed('用户认证失败')

        return ('alex','123')

    def authenticate_header(self,request):
        pass



class DogView(APIView):

    authentication_classes = [MyAuthentication]
    def get(self,request):
        return HttpResponse('获取')

    def post(self,request):
        return HttpResponse('创建')

    def put(self,request):
        return HttpResponse('修改')

    def delete(self,request):
        return HttpResponse('删除')
