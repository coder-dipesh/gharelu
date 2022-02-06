from django.urls import path
from . import views

urlpatterns = [
    # path('error404',views.error404, name='error404'),
    path('',views.homepage, name='homepage'),
    path('about',views.about, name='about'),
    path('service',views.service,name='service'),

    # path('footer',views.footer,name='footer'),

    path('review',views.review,name='review'),

]