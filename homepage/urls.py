from django.urls import path
from . import views

urlpatterns = [
    # path('error404',views.error404, name='error404'),
    path('',views.homepage, name='homepage'),
    path('about',views.about, name='about'),
    path('service',views.service,name='service'),

    # path('footer',views.footer,name='footer'),

    path ('giveFeedback',views.give_feedback),
    path ('get_feedback',views.get_feedback),
]