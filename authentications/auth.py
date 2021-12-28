from django.http import HttpResponse
from django.shortcuts import redirect



def unauthenticated_user(view_function):

    def wrapper_function(request, *args, **kwargs):

        if request.user.is_authenticated:

            return redirect('/')

        else:

            return view_function(request, *args, **kwargs)

    return wrapper_function


def admin_only(view_function):

    def wrapper_function(request, *args, **kwargs):

        if request.user.is_staff and request.user.is_superuser:

            return view_function(request, *args, **kwargs)

        elif request.user.is_staff and not request.user.is_superuser:

            return redirect('/professionals')
        
        elif not request.user.is_staff and not request.user.is_superuser:
            return redirect('/customers')

    return wrapper_function



def customer_only(view_function):

    def wrapper_function(request, *args, **kwargs):

        if not request.user.is_staff and not request.user.is_superuser:

            return view_function(request, *args, **kwargs)

        elif request.user.is_staff and  request.user.is_superuser:

            return redirect('/admins')
        
        elif  request.user.is_staff and not request.user.is_superuser:
            return redirect('/professionals')

    return wrapper_function


def professional_only(view_function):

    def wrapper_function(request, *args, **kwargs):

        if request.user.is_staff and not request.user.is_superuser:

            return view_function(request, *args, **kwargs)

        elif request.user.is_staff and  request.user.is_superuser:

            return redirect('/admins')
        
        elif  not request.user.is_staff and not request.user.is_superuser:
            return redirect('/customers')

    return wrapper_function