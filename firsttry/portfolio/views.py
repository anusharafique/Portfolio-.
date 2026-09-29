from django.shortcuts import render

def home(request):
    return render(request, 'portfolio/portfolio.html')

def coffee(request):
    return render(request, 'portfolio/index.html')