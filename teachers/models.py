from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name
