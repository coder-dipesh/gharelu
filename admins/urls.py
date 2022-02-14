from django.urls import path
from admins import views

urlpatterns = [
    path('',views.adminDashboard, name='admins'),


    path('category/', views.allCategory, name='category' ),
    path('category_form', views.category_form, name='category_form'),

    path ('get_feedback',views.get_feedback, name='get_feedback'),
    path ('get_allservices',views.get_allservices, name='get_allservices'),
    path ('get_allorders',views.get_allorders, name='get_allorders'),


    path('delete_category/<int:category_id>', views.delete_category, name='delete_category'),
    path('update_category/<int:category_id>', views.category_update_form, name='update_category'),

    path('alladmins/', views.allAdmins, name='alladmins' ),
    path('demote_to_customer/<int:user_id>', views.demoteToCustomer, name='demote_to_customer'),
    path('demote_to_professional/<int:user_id>', views.demoteToProfessional, name='demote_to_professional'),

    path('deactivate/<int:user_id>', views.deactivate, name='deactivate'),
    path('reactivate/<int:user_id>', views.reactivate, name='reactivate'),

]