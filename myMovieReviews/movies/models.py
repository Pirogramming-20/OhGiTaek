from django.db import models

# Create your models here.
class Movie(models.Model):
  CHOICES = (
        ('스릴러 영화', '스릴러 영화'),
        ('코미디 영화','코미디 영화'),
        ('액션 영화', '액션 영화'),
        ('sf 영화','sf 영화'),
        ('로맨스 영화','로맨스 영화'),
        ('공포 영화','공포 영화'),
        ('전쟁 영화', '전쟁 영화'),
        ('테스트','테스트'),
    )
  title = models.CharField(max_length=32)
  release_time = models.CharField(max_length=32)
  director = models.CharField(max_length=32)
  actor = models.CharField(max_length=32)
  genre = models.CharField(max_length=32, choices=CHOICES)
  star = models.CharField(max_length=32)
  time = models.CharField(max_length=32)
  content =  models.TextField()
