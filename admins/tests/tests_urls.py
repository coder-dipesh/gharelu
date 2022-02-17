from django.test import SimpleTestCase
from django.urls import reverse,resolve
from admins.views import *

class TestUrls(SimpleTestCase):
    def test_admin_dashboard_urls_is_resolved(self):
      url=reverse('admins')
      view=resolve(url).func
      self.assertEquals(view,adminDashboard)

    def test_category_urls_is_resolved(self):
      url=reverse('category')
      view=resolve(url).func
      self.assertEquals(view,allCategory)

    def test_category_form_urls_is_resolved(self):
      url=reverse('category_form')
      view=resolve(url).func
      self.assertEquals(view,category_form)
    
    def test_get_feedback_urls_is_resolved(self):
      url=reverse('get_feedback')
      view=resolve(url).func
      self.assertEquals(view,get_feedback)
    
    def test_get_allservices_urls_is_resolved(self):
      url=reverse('get_allservices')
      view=resolve(url).func
      self.assertEquals(view,get_allservices)

    def test_get_allorders_urls_is_resolved(self):
      url=reverse('get_allorders')
      view=resolve(url).func
      self.assertEquals(view,get_allorders)

    def test_delete_category_urls_is_resolved(self):
      url=reverse('delete_category',args=[1])
      view=resolve(url).func
      self.assertEquals(view,delete_category)

    def test_update_category_urls_is_resolved(self):
      url=reverse('update_category',args=[1])
      view=resolve(url).func
      self.assertEquals(view,category_update_form)

    def test_alladmins_urls_is_resolved(self):
      url=reverse('alladmins')
      view=resolve(url).func
      self.assertEquals(view,allAdmins)
    
    def test_demote_to_customer_urls_is_resolved(self):
      url=reverse('demote_to_customer',args=[1])
      view=resolve(url).func
      self.assertEquals(view,demoteToCustomer)
    
    def test_demote_to_professional_urls_is_resolved(self):
      url=reverse('demote_to_professional',args=[1])
      view=resolve(url).func
      self.assertEquals(view,demoteToProfessional)
    
    def test_deactivate_urls_is_resolved(self):
      url=reverse('deactivate',args=[1])
      view=resolve(url).func
      self.assertEquals(view,deactivate)
    
    def test_reactivate_urls_is_resolved(self):
      url=reverse('reactivate',args=[1])
      view=resolve(url).func
      self.assertEquals(view,reactivate)
