from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def base(request):
  return render(request, 'base.html')
# Create your views here.
