from django.urls import path

from . import views

urlpatterns = [
    path("new-group", views.create_group, name="new_group"),
    path("update-group/<int:id>", views.update_group, name="update_group"),
    path("delete-group/<int:id>", views.delete_group, name="delete_group"),
    path("groups", views.get_groups_list, name="groups_list"),
]
