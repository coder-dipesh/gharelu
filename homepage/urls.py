from django.urls import path
from . import views

urlpatterns = [
    # path('',views.home, name='home'),
    path('',views.homepage, name='homepage'),

    # path('',),
    # path('',),
    # path('',),
    path('about',views.about, name='about'),

]