from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts' : posts}) # 'posts'라는 변수에 posts객체 전달