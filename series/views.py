from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import Serie

# Create your views here.

def index(request):
    series = Serie.objects.all()

    context = {
        'series': series
    }
    return render(request, 'series/list.html', context)

def detail(request, serie_id):
    serie = get_object_or_404(Serie, pk = serie_id)
    context = {
        'serie': serie
    }
    return render(request, 'series/detail.html', context)

def search(request):
    return render(request, 'series/search.html')

