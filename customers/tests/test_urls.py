from django.test import SimpleTestCase
from django.urls import reverse,resolve
from customers.views import *

class TestUrls(SimpleTestCase):
    def test_customerDashboard_is_resolved(self):
      url=reverse('customers')
      view=resolve(url).func
      self.assertEquals(view,customerDashboard)
    
    def test_customerProfile_is_resolved(self):
      url=reverse('customerprofile')
      view=resolve(url).func
      self.assertEquals(view,customerProfile)

    def test_customerUpdateProfile_is_resolved(self):
      url=reverse('customerupdateprofile')
      view=resolve(url).func
      self.assertEquals(view,customerUpdateProfile)
    
    def test_myBookings_is_resolved(self):
      url=reverse('my_bookings')
      view=resolve(url).func
      self.assertEquals(view,myBookings)

    def test_feedbackForm_is_resolved(self):
      url=reverse('feedback_form',args=[1])
      view=resolve(url).func
      self.assertEquals(view,feedbackForm)

      