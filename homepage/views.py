from django.shortcuts import redirect, render
from django.contrib import messages

from .forms import FeedbackForm


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

@login_required
def review(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Feedback sucessfully Sent")
            return redirect('/mandala_circle/contact')
        else:
            messages.add_message(request, messages.ERROR, "Unable to Send Feedback")
            return render(request, 'mandala_circle/giveFeedback.html', {'form_feedback': form})
    return render(request,'homepage/review.html')
    
def footer(request):
    return render(request,'footer.html')
