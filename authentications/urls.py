from django.urls import path
from . import views


urlpatterns = [
    path('login',views.loginPage, name='login'),
    path('signup',views.signup, name='signup'),
    path('home',views.home, name='home'),



]