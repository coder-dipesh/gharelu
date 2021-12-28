from django.urls import path
from . import views

urlpatterns = [
    path('',views.professionalDashboard, name='professionals'),
    # path('',),
    # path('',),
    # path('',),

]