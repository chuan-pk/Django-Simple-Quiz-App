from django.db import models

# Create your models here.
class Question(models.Model):
    text = models.TextField(default='')
    ans = models.TextField(default='')
