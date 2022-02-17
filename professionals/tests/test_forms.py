from django.test import SimpleTestCase
from professionals.forms import  *


class TestForms(SimpleTestCase):
    def test_service_form(self):
        form=ServiceForm(data={
            'service_name':'Carpenter',
            'service_description ':'I fix furnitures.',
            'service_category':'CARPENTERY',
            'service_photo':'carp.jpg',
            'service_price':'200',
            'service_location':'Kathmandu, Nepal',

        })
        self.assertTrue(form.is_valid())

    def test_service_form(self):
        form=ServiceForm(data={})
      
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),5)



