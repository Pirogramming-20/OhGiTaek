from django.db import models
from apps.users.models import User

# Create your models here.
class Comment(models.Model):
  comment = models.TextField()
  post_id = models.IntegerField()
  user = models.ForeignKey(User, on_delete=models.CASCADE,)


