from django.urls import path, include
from .views import *


urlpatterns = [
    path('', movies_list),
    path("create/",movies_create),
    path("<int:pk>/",movies_read),
    path("<int:pk>/update/", movies_update),
    path("<int:pk>/delete/",movies_delete),
]