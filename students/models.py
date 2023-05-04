from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    year = models.IntegerField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name
