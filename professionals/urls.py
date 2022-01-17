from django.urls import path
from . import views

urlpatterns = [
    path('',views.professionalDashboard, name='professionals'),
    path('professionalprofile',views.professionalProfile, name='professionalprofile'),
    path('professionalupdateprofile',views.professionalUpdateProfile, name='professionalupdateprofile'),

    # path('',),
    # path('',),

]