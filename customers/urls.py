from django.urls import path
from . import views

urlpatterns = [
    path('',views.customerDashboard, name='customers'),
    # path('',),
    # path('',),
    # path('',),

]