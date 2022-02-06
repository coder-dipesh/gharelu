from django.shortcuts import render

def home(request):
    return render(request,'homepage/home.html')


def error404(request, exception):
    return render(request,'error404.html')


def homepage(request):
    return render(request,'homepage/homepage.html')

def about(request):
    return render(request,'homepage/about.html')

def service(request):
    return render(request,'homepage/service.html')

def review(request):
    return render(request,'homepage/review.html')
