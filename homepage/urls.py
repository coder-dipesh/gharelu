from django.urls import path
from homepage import views

urlpatterns = [
    # path('error404',views.error404, name='error404'),
    path('',views.homepage, name='homepage'),
    path('about',views.about, name='about'),

    
    path('service',views.service,name='service'),
    path('book-service/<int:service_id>',views.bookService,name='book-service'),
    path('cancel-service-booking/<int:service_id>',views.cancelBookingService,name='cancel-service-booking'),



    path('review',views.review,name='review'),
]