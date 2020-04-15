from django.conf.urls import url

from api import views

urlpatterns = [
    url(r'^v1/auth/$',views.AuthView.as_view())
]