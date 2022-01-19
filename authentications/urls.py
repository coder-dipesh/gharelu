from django.urls import path
from . import views


urlpatterns = [
    path('signin',views.signin, name='signin'),
    path('usersignup',views.userSignup, name='usersignup'),
    path('prosignup',views.proSignup, name='prosignup'),
    path('reset-password-enterusername',views.entermailResetpassword, name='reset-password-enterusername'),
    path('reset-password/<token>/',views.resetPassword, name='reset-password'),
    path('reset-password-done',views.resetpasswordDone, name='reset-password-done'),

    path('signout',views.signout, name='signout'),

]