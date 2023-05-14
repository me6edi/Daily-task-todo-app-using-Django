from django.db import models
from datetime import datetime

# Create your models here.
class Task(models.Model):
    content = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now())
    complete = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.content