from django.shortcuts import render



def home(request):
    return render(request,'homepage/home.html')


def homepage(request):
    return render(request,'homepage/homepage.html')

def about(request):
    return render(request,'homepage/about.html')