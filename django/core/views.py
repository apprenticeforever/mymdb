from django.views.generic import (
	ListView,
	DetailView,)
from core.models import Movie
from django.shortcuts import render

class MovieList(ListView):
	model = Movie

class MovieDetail(DetailView):
	model = Movie