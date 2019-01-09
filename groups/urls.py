from django.urls import path

from . import views

urlpatterns = [
    path('info/<u_id>', views.info_page, name="info"),
    path('id/<u_id>', views.group, name="group"),
    path('create-group', views.create_group, name="create_group"),
]
