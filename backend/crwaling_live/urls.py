from django.urls import path, include
from crwaling_live import views
urlpatterns = [
    path(r'crwaling',views.crwaling),
    path(r'uploader',views.uploader),
]