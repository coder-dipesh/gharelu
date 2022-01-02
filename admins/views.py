from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from authentications.auth import admin_only


@login_required
@admin_only
def adminDashboard(request):
    return render(request, 'admins/adminDashboard.html' )