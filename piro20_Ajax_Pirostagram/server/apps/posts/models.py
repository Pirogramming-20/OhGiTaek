from django.db import models
from apps.comments.models import *
# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=24)
  content = models.TextField()
  like = models.IntegerField(default = 0)
  comments = models.ManyToManyField(Comment, blank=True)
  photo = models.ImageField('이미지', blank=True, upload_to='posts/%Y%m%d')

  def post_comment(self):
    return self.comments.filter(post_id=self.id)
