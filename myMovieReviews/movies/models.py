from django.db import models

# Create your models here.
class Movie(models.Model):
  title = models.CharField(max_length=32)
  release_time = models.CharField(max_length=32)
  director = models.CharField(max_length=32)
  actor = models.CharField(max_length=32)
  genre = models.CharField(max_length=32)
  star = models.CharField(max_length=32)
  time = models.CharField(max_length=32)
  content =  models.TextField()
