from django.db import models

# Create your models here.
class Comment(models.Model):
  comment = models.TextField()
  post_id = models.IntegerField()


