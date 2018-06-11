from django.db import models

# Create your models here.
class Question(models.Model):
    text = models.TextField(default='')
    ans = models.TextField(default='')
    count = models.IntegerField(default=0)
    correct_count = models.IntegerField(default=0)