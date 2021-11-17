from django.urls import path, include
from crwaling_live import views
urlpatterns = [
    path(r'covid',views.covid),
]