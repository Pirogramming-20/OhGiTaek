from django.db import models
from apps.comments.models import *
# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=24)
  content = models.TextField()
  like = models.IntegerField()
  comments = models.ManyToManyField(Comment, blank=True)

  def post_comment(self):
    return self.comments.filter(post_id=self.id)
