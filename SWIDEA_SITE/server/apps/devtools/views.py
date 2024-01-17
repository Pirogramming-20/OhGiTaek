from django.shortcuts import render, redirect
from .models import Devtool
from .forms import DevForm
# Create your views here.

def dev_list(request):
  devtools = Devtool.objects.all()
  
  ctx = {
    'devtools':devtools
  }
  return render(request,'devtools/devtool_list.html',ctx)

def create(request):
  if request.method == 'GET':
    form = DevForm()
    ctx = {'form' : form}
    return render(request,'devtools/devtool_create.html',ctx)
  
  form = DevForm(request.POST,  request.FILES)
  if form.is_valid():
    form = form.save()
  return redirect('devtools:detail',form.id)

def detail(request,pk):
  devtool = Devtool.objects.get(id=pk)

  related_ideas = devtool.idea_set.all()
  ctx = {'devtool':devtool, 'related_ideas':related_ideas}
  return render(request,'devtools/devtool_detail.html',ctx)

def update(request,pk):
  devtool = Devtool.objects.get(id=pk)
  if request.method == 'GET':
    #폼이 남아있는 상태로 보이도록함
    form = DevForm(instance=devtool)
    ctx = {
      'form' : form,
      'pk':pk
    } 
    return render(request,'devtools/devtool_update.html',ctx)
  
  #업데이트
  form = DevForm(request.POST,instance=devtool)
  if form.is_valid():
    form.save()
  return redirect('devtools:detail',pk)

def delete(request,pk):
  if request.method == 'POST':
    Devtool.objects.get(id=pk).delete()
  return redirect('devtools:list')
