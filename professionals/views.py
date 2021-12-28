from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from authentications.auth import professional_only

# Create your views here.

@login_required
@professional_only
def professionalDashboard(request):
    return render(request, 'professionals/professionalDashboard.html')