from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.adminDashboard, name='admins'),
    path('orders/', views.allOrders, name='orders' ),
    # path('',),

]