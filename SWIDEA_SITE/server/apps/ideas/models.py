from django.db import models
from apps.devtools.models import *
# Create your models here.
class Idea(models.Model):
  title = models.CharField('제목',max_length=24)
  image = models.ImageField('이미지', blank=True, upload_to='ideas/%Y%m%d')
  content = models.TextField('아이디어 설명')
  interest = models.IntegerField('아이디어 관심도',default=0)
  updated_date = models.DateTimeField('수정일', auto_created=True,auto_now=True)
  #수정필요
  devtool = models.ForeignKey(Devtool,on_delete=models.CASCADE,verbose_name = '개발툴')
  
  
  def __str__(self):
    return self.title