from django.conf.urls import url

from app01 import views

urlpatterns=[
    # url('^index/',views.index),
    # url('^student/',views.StudentsView.as_view()),
    # url('^order/',views.OrderView.as_view()),


    url('^dog/',views.DogView.as_view())

]