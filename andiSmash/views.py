from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    template_name = 'home.html'
    context = {
        'title': 'my home',
        'welcome': 'welcome to my home',
    }
    return render(request, template_name, context)

def about(request):
    template_name = 'about.html'
    context = {
        'title': 'about me',
        'welcome': 'ini page about',
    }
    return render(request, template_name, context)