from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from authentications.auth import admin_only
from django.contrib import messages
from django.contrib.auth.models import User

@login_required
@admin_only
def adminDashboard(request):

    users = User.objects.all()

    user_count = users.filter(is_staff=0).count()
    admin_count = users.filter(is_superuser=1).count()
    professional_count = users.filter(is_staff=1,is_superuser=0).count()

    user_info = users.filter(is_staff=0)
    admin_info = users.filter(is_superuser=1)
    professional_info = users.filter(is_staff=1,is_superuser=0)


    context = {
        'user': user_count,
        'admin': admin_count,
        'professional':professional_count,
        'user_info': user_info,
        'admin_info': admin_info,
        'professional_info':professional_info,
        'activate_adminhome': 'active bg-primary'
    }
    return render(request, 'admins/adminDashboard.html' , context )


def allOrders(request):
    
    context = {
        'activate_orders': 'active bg-primary'
    }

    return render(request, 'admins/orders.html' , context)
