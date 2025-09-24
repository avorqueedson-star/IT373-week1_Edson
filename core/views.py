from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Announcement

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def base(request):
    return render(request, 'base.html')

def announcements_list(request):
    announcements = Announcement.objects.filter(is_published=True)
    return render(request, 'announcements_list.html', {'announcements': announcements})

def announcements_detail(request, id):
    announcement = get_object_or_404(Announcement, id=id, is_published=True)
    return render(request, 'announcements_detail.html', {'announcement': announcement})

def custom_404(request, exception):
    return render(request, '404.html', status=404)
