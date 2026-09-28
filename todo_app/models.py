from django.db import models

# Create your models here.
class todo_model(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField()
