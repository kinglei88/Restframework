from django.conf.urls import url

from api import views

urlpatterns = [
    # url(r'^index/$',views.User.as_view())
    url(r"^(?P<version>[v1|v2|v3]+)/index/$",views.User.as_view())

]