from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from admins.forms import CategoryForm
from admins.models import Category
from authentications.auth import admin_only
from django.contrib import messages
from django.contrib.auth.models import User

@login_required
@admin_only
def adminDashboard(request):

    users = User.objects.all()
    category = Category.objects.all()

    user_count = users.filter(is_staff=0).count()
    admin_count = users.filter(is_superuser=1).count()
    professional_count = users.filter(is_staff=1,is_superuser=0).count()

    user_info = users.filter(is_staff=0)
    admin_info = users.filter(is_superuser=1)
    professional_info = users.filter(is_staff=1,is_superuser=0)

    totalCategory =category.count()


    context = {
        'user': user_count,
        'admin': admin_count,
        'professional':professional_count,
        'user_info': user_info,
        'admin_info': admin_info,
        'professional_info':professional_info,
        'category':totalCategory,
        'activate_adminhome': 'active bg-primary'
    }
    return render(request, 'admins/adminDashboard.html' , context )

@login_required
@admin_only
def allOrders(request):
    
    context = {
        'activate_orders': 'active bg-primary'
    }

    return render(request, 'admins/orders.html' , context)

@login_required
@admin_only
def allCategory(request):
    categories = Category.objects.all().order_by('-id')
    context = {
        'categories': categories,
        'activate_category': 'active'
    }
    return render(request, 'admins/category.html', context)

    

@login_required
@admin_only
def category_form(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Category added Successfully')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add Category')
            return render(request, 'admins/category_form.html', {'form_category': form})
    
    context = {
        'form_category': CategoryForm,
        'activate_category': 'active bg-primary'
        }

    return render(request, 'admins/category_form.html' , context)


@login_required
@admin_only
def category_update_form(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Category Updated Successfully')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add Category')
            return render(request, 'admins/category_update_form.html', {'form_category': form})

    context = {
        'form_category': CategoryForm(instance=category),
        'activate_category': 'active',
    }
    return render(request, 'admins/category_update_form.html', context)



@login_required
@admin_only
def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    messages.add_message(request, messages.SUCCESS, 'Category deleted successfully')
    return redirect('/admins/category')


@login_required
@admin_only
def allAdmins(request):
    
    context = {
        'activate_admins': 'active bg-primary'
    }

    return render(request, 'admins/allAdmins.html' , context)