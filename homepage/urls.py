from django.urls import path
from . import views

urlpatterns = [
    # path('error404',views.error404, name='error404'),
    path('',views.homepage, name='homepage'),

    # path('',),
    # path('',),
    # path('',),
    path('about',views.about, name='about'),

     # path('',),
    # path('',),
    # path('',),
    path('service',views.service,name='service'),

     # path('',),
    # path('',),
    # path('',),
    path('review',views.review,name='review')

]