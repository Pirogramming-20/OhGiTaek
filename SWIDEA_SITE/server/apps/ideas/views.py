import json
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import *
from .forms import IdeaForm
from django.core.paginator import Paginator

# Create your views here.
sort_temp='temp'
def idea_list(request):
  ideas = Idea.objects.all()
  sort = request.GET.get('sort')
  print(request.GET.get('sort'))
  if (request.GET.get('sort')) is None:
    global sort_temp
    if sort_temp == 'temp':
      sort = 'temp'
    else:
      sort = sort_temp
  else:
    sort = request.GET.get('sort')
  
  if sort == 'title':
    ideas = ideas.order_by('title')
  elif sort == 'pk':
    ideas= ideas.order_by('pk')
  elif sort == 'updated_date':
    ideas = ideas.order_by('-pk')
  elif sort == 'interest':
    ideas = ideas.order_by('-interest')
  elif sort == 'star':
    ideas = ideas.order_by('-star')
  paginator = Paginator(ideas, 4) # 한 페이지에 4개의 게시글을 보여줌
  page = request.GET.get('page')
  ideas = paginator.get_page(page)
  sort_temp = sort
  ctx = {
    'ideas':ideas,
    'paginator': paginator,
    
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