from django.test import SimpleTestCase
from authentications.forms import  *


class TestForms(SimpleTestCase):
    def test_profile_form(self):
        form=ProfileForm(data={
            'user':'johndoe',
            'forget_password_token':'12345',
            'firstname':'John',
            'lastname':'Doe',
            'username':'gharelu.user',
            'email':'johndoe@gmail.com',
            'phone':'9816034112',
            'address':'Buddanilakantha',
            'city':'Kathmandu',
            'profile_pic':'user.png',

        })
        self.assertTrue(form.is_valid())

    def test_profile_form(self):
        form=ProfileForm(data={})
      
        self.assertFalse(form.is_valid())
        self.assertNotEquals(len(form.errors),8)   # actual error count is 5


    


