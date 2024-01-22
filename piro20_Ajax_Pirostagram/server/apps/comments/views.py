from django.shortcuts import render,redirect

from apps.posts.models import Post
from .models import *
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create(request):
  req = json.loads(request.body)
  postId = req['id']
  print('1')
  userName = req['username']
  print('2')
  post = Post.objects.get(id=postId)
  user1 = User.objects.get(username = userName)
  print(user1)
  comment = Comment.objects.create(
    user = user1,
    comment = req["comment"],
    post_id = postId,
  )
  comment_id = comment.id
  post.comments.add(comment)
  return JsonResponse({'id':postId,'comment':req["comment"], 'comment_id':comment_id, 'user':comment.user.username})





@csrf_exempt
def delete(request, pk):
  req = json.loads(request.body)
  comment_id = req['comment_id']
  comment = Comment.objects.get(id=comment_id)
  comment.delete()
  return JsonResponse({'id':pk,'comment_id':comment_id})

