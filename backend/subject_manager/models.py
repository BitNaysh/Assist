from django.db import models

priority_dict = {(1, 1): 4, (1, 2): 4, (1, 3): 5, (1, 4): 5, (1, 5): 5, (2, 1): 3, (2, 2): 3, (2, 3): 4, (2, 4): 5, (2, 5): 5, (3, 1): 2, (3, 2): 2, (3, 3): 3, (3, 4): 4, (3, 5): 4, (4, 1): 1, (4, 2): 1, (4, 3): 2, (4, 4): 3, (4, 5): 3}

class Assignment(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateTimeField()
    grade = models.IntegerField(max_length=5)
    credits = models.IntegerField(max_length=4)
    priority = models.IntegerField(max_length=5)
    try:
        priority = models.IntegerField(priority_dict[(credits, grade)])
    except:
        priority = 0
