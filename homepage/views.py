from django.shortcuts import render



def error404(request):
    return render(request,'error404.html')


def homepage(request):
    return render(request,'homepage/homepage.html')
