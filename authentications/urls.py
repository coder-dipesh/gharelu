from django.urls import path
from . import views


urlpatterns = [
    path('signin',views.signin, name='signin'),
    path('signup',views.signup, name='signup'),
    path('pro-signup',views.proSignup, name='pro-signup'),
    path('signout',views.signout, name='signout'),
]