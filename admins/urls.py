from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.adminDashboard, name='admins'),
    path('adminprofile',views.adminProfile,name='adminprofile'),
    # path('',),
    # path('',),

]