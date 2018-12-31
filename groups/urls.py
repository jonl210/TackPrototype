from django.urls import path

from . import views

urlpatterns = [
    path('id/<u_id>', views.group, name="group"),
    path('create-group', views.create_group, name="create_group"),
]
