from django.urls import path
from . import views

urlpatterns = [
    path('',views.customerDashboard, name='customers'),
    path('customerprofile',views.customerProfile, name='customerprofile'),
    path('customerupdateprofile',views.customerUpdateProfile, name='customerupdateprofile'),
    

]