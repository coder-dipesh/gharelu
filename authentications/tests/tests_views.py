from django.test import TestCase,Client
from django.urls import reverse


# Here we are testing the views ..
#  we test if views are rendering correct templates or not
# we get urls via reverse function and pass value to .assertTemplateUsed with expeted template with actual template

class Test_views(TestCase):
    def test_signin(self):
        client=Client()
        response=client.get(reverse('signin'))
        # self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'account/login.html')
    
    def test_usersignup(self):
        client=Client()
        response=client.get(reverse('usersignup'))
        self.assertTemplateUsed(response,'account/signup.html')

    def test_prosignup(self):
        client=Client()
        response=client.get(reverse('prosignup'))
        self.assertTemplateUsed(response,'account/signup.html')

    def test_reset_password_enterusername(self):
        client=Client()
        response=client.get(reverse('reset-password-enterusername'))
        self.assertTemplateUsed(response,'account/reset-password-enterusername.html')

    def test_reset_password_done(self):
        client=Client()
        response=client.get(reverse('reset-password-done'))
        self.assertTemplateUsed(response,'account/reset-password-done.html')
    
    def test_change_password(self):
        client=Client()
        response=client.get(reverse('change-password'))
        self.assertTemplateUsed(response,'account/change-password.html')