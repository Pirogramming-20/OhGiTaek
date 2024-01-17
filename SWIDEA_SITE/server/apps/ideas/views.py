import json
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import *
from .forms import IdeaForm
# Create your views here.

def idea_list(request):
  ideas = Idea.objects.all()
  sort = request.GET.get('sort')
  if sort == 'title':
    ideas = ideas.order_by('title')
  elif sort == 'pk':
    ideas= ideas.order_by('pk')
  elif sort == 'updated_date':
    ideas = ideas.order_by('updated_date')
  elif sort == 'interest':
    ideas = ideas.order_by('interest')
  ctx = {
    'ideas':ideas
  }
  return render(request,'ideas/idea_list.html',ctx)

def create(request):
  if request.method == 'GET':
    form = IdeaForm()
    ctx = {'form' : form}
    return render(request,'ideas/idea_create.html',ctx)
  
  form = IdeaForm(request.POST,  request.FILES)
  if form.is_valid():
    form = form.save()
  return redirect('ideas:detail',form.id)

def detail(request,pk):
  idea = Idea.objects.get(id=pk)
  
  ctx = {'idea':idea}
  return render(request,'ideas/idea_detail.html',ctx)

def update(request,pk):
  idea = Idea.objects.get(id=pk)
  if request.method == 'GET':
    #폼이 남아있는 상태로 보이도록함
    form = IdeaForm(instance=idea)
    ctx = {
      'form' : form,
      'pk':pk
    } 
    return render(request,'ideas/idea_update.html',ctx)
  
  #업데이트
  form = IdeaForm(request.POST,request.FILES,instance=idea)
  if form.is_valid():
    form.save()
  return redirect('ideas:detail',pk)

def interest(request):
  pk = request.POST.get('pk', None) # ajax 통신을 통해서 template에서 POST방식으로 전달
  check = request.POST.get('check', None)
  idea = get_object_or_404(Idea, id=pk)
  if check == 'increase':
    idea_interest = idea.interest + 1
    idea.interest += 1
  else:
    idea_interest = idea.interest - 1
    idea.interest -= 1
  idea.save()
  context = {'interest' : idea_interest }
  return HttpResponse(json.dumps(context), content_type="application/json")
  # context를 json 타입으로



def delete(request,pk):
  if request.method == 'POST':
    Idea.objects.get(id=pk).delete()
  return redirect('ideas:list')


def star_list(request,pk):
  star_toggle = Idea.objects.get(id=pk)
  if star_toggle.star:
    star_toggle.star = False
  else:
    star_toggle.star = True
  star_toggle.save()
  return redirect('ideas:list')

def star_detail(request,pk):
  star_toggle = Idea.objects.get(id=pk)
  if star_toggle.star:
    star_toggle.star = False
  else:
    star_toggle.star = True
  star_toggle.save()
  return redirect('ideas:detail',pk)