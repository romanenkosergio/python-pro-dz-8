from django.urls import path

from . import views

urlpatterns = [
    path("new-teacher", views.teacher_create, name="new_teacher"),
    path("update-teacher/<int:id>", views.update_teacher, name="update_teacher"),
    path("delete-teacher/<int:id>", views.delete_teacher, name="delete_teacher"),
    path("teachers", views.get_teachers_list, name="teachers_list"),
]
