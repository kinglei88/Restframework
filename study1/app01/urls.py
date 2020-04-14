from django.conf.urls import url

from app01 import views

urlpatterns=[
    url('^index/',views.index),
    url('^student/',views.StudentsView.as_view())
]