import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


def index(request):

    user_list = ['hello','world']


    return HttpResponse(json.dumps(user_list))


class StudentsView(View):

    def get(self,request,*args,**kwargs):
        return HttpResponse('GET')

    def post(self,request,*args,**kwargs):
        return HttpResponse('POST')


    def put(self,request,*args,**kwargs):
        return HttpResponse('PUT')


    def delete(self,request,*args,**kwargs):
        return HttpResponse('DELETE')