from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey("teachers.Teacher", on_delete=models.CASCADE)
    students = models.ManyToManyField("students.Student", related_name="groups")

    def __str__(self):
        return self.name
