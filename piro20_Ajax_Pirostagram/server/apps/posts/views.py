from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
# Create your views here.

def main(request):
  posts = Post.objects.all().order_by('id')
  for post in posts:
    post.is_like = post.user_liked(request.user)
  ctx = {
    'posts' : posts
  }
  return render(request,'posts/main.html',ctx)

def create(request):
  if request.method == 'POST':
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
      post = form.save(commit=False)  
      post.user = request.user  
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
  post.is_like=post.user_liked(request.user)
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
    post_like = req['like']
    post_username = req['username']
    post = Post.objects.get(id=post_id)
    user = User.objects.get(username=post_username)

    
    if post.user_liked(user):
      post.likes.remove(user)
      post.like -= 1
    else:
      post.likes.add(user)
      post.like += 1
    post.save()
    
    return JsonResponse({'id':post_id,'type':post.user_liked(user),'like':post.like})