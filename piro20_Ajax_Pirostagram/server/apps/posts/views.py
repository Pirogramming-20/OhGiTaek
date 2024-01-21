from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
# Create your views here.

def main(request):
  posts = Post.objects.all().order_by('id')
  ctx = {
    'posts' : posts
  }
  return render(request,'posts/main.html',ctx)

def create(request):
  if request.method == 'POST':
    post = PostForm(request.POST)
    if post.is_valid():
      post.save()
      return redirect('posts:main')
    else:
      ctx={
        'post':post,
      }
      return render(request, 'post/create.html',ctx)
  else:
    post = PostForm()
    ctx={
        'post': post,
    }
    return render(request, 'posts/create.html', ctx)

def detail(request,pk):
  post = get_object_or_404(Post, pk=pk)
  comments = post.comments.all()
  ctx = {
    'comments':comments,
    "post" : post,
  }
  return render(request, "posts/detail.html", ctx)


########## ajax
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def like_ajax(request):
    req = json.loads(request.body)
    post_id = req['id']

    post = Post.objects.get(id=post_id)

    post.like += 1
    post.like = post.like%2
    post.save()
    
    return JsonResponse({'id':post_id,'type':post.like})