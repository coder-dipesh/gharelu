from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from authentications.auth import customer_only

# Create your views here.

@login_required
@customer_only
def customerDashboard(request):
    return render(request, 'customers/customerDashboard.html')