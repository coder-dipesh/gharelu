from django.urls import path
from . import views


urlpatterns = [
    path('signin',views.signin, name='signin'),
    path('usersignup',views.userSignup, name='usersignup'),
    path('prosignup',views.proSignup, name='prosignup'),
    path('signout',views.signout, name='signout'),

]