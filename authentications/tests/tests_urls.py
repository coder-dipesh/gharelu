from django.test import SimpleTestCase
from django.urls import reverse,resolve
from authentications.views import *

class TestUrls(SimpleTestCase):
    def test_signin_urls_is_resolved(self):
      url=reverse('signin')
      view=resolve(url).func
      self.assertEquals(view,signin)

    def test_usersignup_urls_is_resolved(self):
      url=reverse('usersignup')
      view=resolve(url).func
      self.assertEquals(view,userSignup)
    
    def test_prosignup_urls_is_resolved(self):
      url=reverse('prosignup')
      view=resolve(url).func
      self.assertEquals(view,proSignup)
    
    def test_reset_password_enterusername_urls_is_resolved(self):
      url=reverse('reset-password-enterusername')
      view=resolve(url).func
      self.assertEquals(view,entermailResetpassword)
    
    def test_reset_password_urls_is_resolved(self):
      url=reverse('reset-password',args=['token'])
      view=resolve(url).func
      self.assertEquals(view,resetPassword)

    def test_reset_password_done_urls_is_resolved(self):
      url=reverse('reset-password-done')
      view=resolve(url).func
      self.assertEquals(view,resetpasswordDone)
    
    def test_change_password_urls_is_resolved(self):
      url=reverse('change-password')
      view=resolve(url).func
      self.assertEquals(view,change_password)

    def test_signout_urls_is_resolved(self):
      url=reverse('signout')
      view=resolve(url).func
      self.assertEquals(view,signout)
    
