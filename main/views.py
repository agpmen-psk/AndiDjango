from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles


def index(request):
    data = {
        'title': 'Соседи',
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def rooms(request):
    return render(request, 'main/rooms.html')


def services(request):
    return render(request, 'main/amenities.html')


def contacs(request):
    return render(request, 'main/contact.html')


def news(request):
    news = Articles.objects.all()
    return render(request, 'main/news.html', {'news': news})
