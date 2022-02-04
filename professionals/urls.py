from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.professionalDashboard, name='professionals'),

    path('professionalprofile',views.professionalProfile, name='professionalprofile'),
    path('professionalupdateprofile',views.professionalUpdateProfile, name='professionalupdateprofile'),

    path('bookings',views.bookings, name='bookings'),
    path('change_password',views.changePassword, name='change_password'),

    path('services',views.service, name='services'),
    path('service_form',views.service_form, name='service_form'),
    path('delete_service/<int:service_id>', views.delete_service, name='delete_service'),
    path('update_service/<int:service_id>', views.service_update_form, name='update_service'),


]