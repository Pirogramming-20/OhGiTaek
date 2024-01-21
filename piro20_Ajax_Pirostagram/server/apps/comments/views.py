from django.shortcuts import render,redirect
from .models import *
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create(request):
  req = json.loads(request.body)
  postId = req['id']
  
  comment_id = Comment.objects.create(
    comment = req["comment"],
    post_id = postId,
  ).id
  return JsonResponse({'id':postId,'comment':req["comment"], 'comment_id':comment_id})


@csrf_exempt
def delete(request, pk):
  req = json.loads(request.body)
  comment_id = req['comment_id']
  comment = Comment.objects.get(id=comment_id)
  comment.delete()
  return JsonResponse({'id':pk,'comment_id':comment_id})

