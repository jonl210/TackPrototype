from django.urls import path

from . import views

urlpatterns = [
    path('upload-photo', views.upload_photo, name="upload"),
]
