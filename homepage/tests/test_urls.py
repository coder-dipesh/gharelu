from django.test import SimpleTestCase
from django.urls import reverse,resolve
from homepage.views import *

class TestUrls(SimpleTestCase):
    def test_homepage_is_resolved(self):
      url=reverse('homepage')
      view=resolve(url).func
      self.assertEquals(view,homepage)

    def test_about_is_resolved(self):
      url=reverse('about')
      view=resolve(url).func
      self.assertEquals(view,about)

    def test_service_is_resolved(self):
      url=reverse('service')
      view=resolve(url).func
      self.assertEquals(view,service)

    def test_book_service_is_resolved(self):
      url=reverse('book-service',args=[1])
      view=resolve(url).func
      self.assertEquals(view,bookService)
    
    def test_cancel_service_booking_is_resolved(self):
      url=reverse('cancel-service-booking',args=[1])
      view=resolve(url).func
      self.assertEquals(view,cancelBookingService)
    
    def test_support_is_resolved(self):
      url=reverse('support')
      view=resolve(url).func
      self.assertEquals(view,Support)
      