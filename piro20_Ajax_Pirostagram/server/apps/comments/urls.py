from django.urls import path
from .views import *

app_name = 'comments'

urlpatterns = [
    path('create/',create,name='create'),
    path('delete/<int:pk>', delete, name='delete'),
]
