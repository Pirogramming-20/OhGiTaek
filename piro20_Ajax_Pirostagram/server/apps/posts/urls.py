from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
    path('',main,name = 'main'),
    path('create/',create,name='create'),
    path('detail/<int:pk>/',detail,name='detail'),
    path('like_ajax/', like_ajax, name='like_ajax'),
]
