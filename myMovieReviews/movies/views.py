from django.shortcuts import render, HttpResponse , redirect, get_object_or_404
from .models import *
# Create your views here.

def movies_list(request):
  movies = Movie.objects.all().order_by(('title'))
  context = {
    "movies" : movies
  }
  return render(request,'movies_list.html',context)

def movies_create(request):
  if request.method == "POST":
    Movie.objects.create(
    title = request.POST["title"],
    release_time = request.POST["release_time"],
    director = request.POST["director"],
    actor = request.POST["actor"],
    genre = request.POST["genre"],
    star = request.POST["star"],
    time = request.POST["time"],
    content =  request.POST["content"],
    )
    return redirect("/movies")
  return render(request,"movies_create.html")

def movies_read(request, pk):
  movie = get_object_or_404(Movie, pk=pk)
  movie_time_hour = int(movie.time) // 60
  movie_time_min = int(movie.time) - (movie_time_hour*60)
  context = {
    "movie" : movie,
    "movie_time_hour" : movie_time_hour,
    "movie_time_min" : movie_time_min,
  }
  return render(request, "movies_read.html", context)

def movies_update(request, pk):
  movie = get_object_or_404(Movie, pk=pk)
  if request.method == 'POST':
    movie.title = request.POST["title"]
    movie.release_time = request.POST['release_time']
    movie.director = request.POST['director']
    movie.actor = request.POST['actor']
    movie.genre = request.POST['genre']
    movie.star = request.POST['star']
    movie.time = request.POST['time']
    movie.content = request.POST['content']
    movie.save()
    return redirect(f"/movies/{movie.id}")
  
  context = {
    'movie' : movie
  }
  return render(request,'movies_update.html', context)

def movies_delete(request,pk):
  if request.method == 'POST':
    movie = Movie.objects.get(id = pk)
    movie.delete()
  return redirect('/movies')