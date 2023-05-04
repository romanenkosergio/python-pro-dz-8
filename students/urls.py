from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("new-student", views.student_create, name="new_student"),
    path("update-student/<int:id>", views.update_student, name="update_student"),
    path("delete-student/<int:id>", views.delete_student, name="delete_student"),
    path("students", views.get_students_list, name="students_list"),
]
