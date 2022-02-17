from django.test import SimpleTestCase
from homepage.forms import  *


class TestForms(SimpleTestCase):
    def test_order_form(self):
        form=OrderForm(data={
            'service':'Carpenter',
            'user ':'John',
            'date':'2021/2/1',
            'start_time':'1:00 AM',
            'end_time':'2:00 AM',
            'total_price':'100',
            'contact_no':'9843060170',
            'contact_address':'Baluwakhani, Kapan',
            'status':'Pending',
        })
        self.assertTrue(form.is_valid())

    def test_order_form(self):
        form=OrderForm(data={})
      
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),5)

    def test_contact_form(self):
        cform=ContactForm(data={
                'name':'John Doe',
                'email ':'johndoe@gmail.com',
                'subject':'More Services',
                'message':'Hello can you please add more services',
            })
        self.assertFalse(cform.is_valid())

    def test_order_form(self):
        cform=ContactForm(data={})
      
        self.assertFalse(cform.is_valid())
        self.assertEquals(len(cform.errors),4)


    


