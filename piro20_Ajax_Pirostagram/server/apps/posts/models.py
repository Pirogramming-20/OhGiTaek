from django.db import models
from apps.comments.models import *
from apps.users.models import User
# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=24)
  content = models.TextField()
  like = models.IntegerField(default = 0)
  comments = models.ManyToManyField(Comment, blank=True)
  photo = models.ImageField('이미지', blank=True, upload_to='posts/%Y%m%d')
  user = models.ForeignKey(User, on_delete=models.CASCADE,)

  def post_comment(self):
    return self.comments.filter(post_id=self.id)
