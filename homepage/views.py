from django.shortcuts import render



def error404(request, exception):
    return render(request,'error404.html')


def homepage(request):
    return render(request,'homepage/homepage.html')

def about(request):
    return render(request,'homepage/about.html')