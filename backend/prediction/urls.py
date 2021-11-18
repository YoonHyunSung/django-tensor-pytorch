from django.conf.urls import url

from prediction import views

urlpatterns =[
    url(r'upload', views.upload),
]