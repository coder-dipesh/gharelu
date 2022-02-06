from django.urls import path
from . import views

urlpatterns = [
    # path('error404',views.error404, name='error404'),
    path('',views.homepage, name='homepage'),
    path('about',views.about, name='about'),
    path('service',views.service,name='service'),
<<<<<<< HEAD

     # path('',),
    # path('',),
    # path('',),
    path('review',views.review,name='review'),

     # path('',),
    # path('',),
    # path('',),
    path('footer',views.footer,name='footer')


=======
    path('footer',views.footer,name='footer'),
>>>>>>> d90c9ad6cac88f229e457d369de40de86f8cd141
]