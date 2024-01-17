from django.urls import path
from .views import *

app_name = 'ideas'
urlpatterns = [
    path('',idea_list,name='list'),
    path('create/',create,name='create'),
    path('detail/<int:pk>/',detail,name='detail'),
    path('delete/<int:pk>/',delete,name='delete'),
    path('update/<int:pk>/',update,name='update'),
    path('star_list/<int:pk>',star_list,name='star_list'),
    path('star_detail/<int:pk>',star_detail,name='star_detail'),
]
