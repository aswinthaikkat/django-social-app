from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(
        User, related_name='blogposts', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
