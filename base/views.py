from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def about(request):
    return render(request, 'base/about.html')

def portfolio(request):
    return render(request, 'base/portfolio.html')

def contact(request):
    return render(request, 'base/contact.html')