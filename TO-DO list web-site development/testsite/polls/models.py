from django.db import models

class To_do(models.Model):
    plan = models.CharField(max_length=200)
    due_date = models.DateTimeField('due date')
    completed = models.BooleanField()
    def __str__(self):
        return self.plan
