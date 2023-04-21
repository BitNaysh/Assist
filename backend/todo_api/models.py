from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    task = models.CharField(max_length = 180)
    grade = models.IntegerField()
    credits = models.IntegerField()

    def __str__(self):
        return self.task