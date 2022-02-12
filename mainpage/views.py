from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import Course

# Create your views here.
def index(request):
    
    data = {
        'courses': Course.objects.all(),
    }
    
    return render(request, 'mainpage/index.html', data)

def about_us(request):
    return render(request, 'mainpage/about_us.html')

def course(request, id):
    
    data = {
        'el': Course.objects.get(id=id),
    }

    return render(request, 'mainpage/course.html', data)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')