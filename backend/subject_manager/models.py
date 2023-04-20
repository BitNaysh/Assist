from django.db import models

class Assignment(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateField()
    grade = models.DecimalField(max_digits=5, decimal_places=2)
