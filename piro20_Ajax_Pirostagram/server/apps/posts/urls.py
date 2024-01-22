from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'posts'

urlpatterns = [
    path('',main,name = 'main'),
    path('create/',create,name='create'),
    path('detail/<int:pk>/',detail,name='detail'),
    path('like_ajax/', like_ajax, name='like_ajax'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)