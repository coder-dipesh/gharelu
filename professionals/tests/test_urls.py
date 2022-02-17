from django.test import SimpleTestCase
from django.urls import reverse,resolve
from professionals.views import *

class TestUrls(SimpleTestCase):
    def test_professional_dashboard_is_resolved(self):
      url=reverse('professionals')
      view=resolve(url).func
      self.assertEquals(view,professionalDashboard)

    def test_professional_profile_is_resolved(self):
      url=reverse('professionalprofile')
      view=resolve(url).func
      self.assertEquals(view,professionalProfile)

    def test_professional_update_profile_is_resolved(self):
      url=reverse('professionalupdateprofile')
      view=resolve(url).func
      self.assertEquals(view,professionalUpdateProfile)
    
    def test_bookings_is_resolved(self):
      url=reverse('bookings')
      view=resolve(url).func
      self.assertEquals(view,bookings)

    def test_approve_booking_is_resolved(self):
      url=reverse('approve-booking',args=[1])
      view=resolve(url).func
      self.assertEquals(view,approveBooking)

    def test_decline_booking_is_resolved(self):
      url=reverse('decline-booking',args=[1])
      view=resolve(url).func
      self.assertEquals(view,declineBooking)

    def test_change_password_is_resolved(self):
      url=reverse('change_password')
      view=resolve(url).func
      self.assertEquals(view,changePassword)

    def test_services_is_resolved(self):
      url=reverse('services')
      view=resolve(url).func
      self.assertEquals(view,service)

    def test_service_form_is_resolved(self):
      url=reverse('service_form')
      view=resolve(url).func
      self.assertEquals(view,service_form)

    def test_delete_service_is_resolved(self):
      url=reverse('delete_service',args=[1])
      view=resolve(url).func
      self.assertEquals(view,delete_service)

    def test_service_update_form_is_resolved(self):
      url=reverse('update_service',args=[1])
      view=resolve(url).func
      self.assertEquals(view,service_update_form)
    
    