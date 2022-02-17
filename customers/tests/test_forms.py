from django.test import SimpleTestCase
from customers.forms import  *


class TestForms(SimpleTestCase):
    def test_feedback_form(self):
        form=FeedbackForm(data={
            'user':'John',
            'service ':'Cleaning',
            'rating':'3',
            'subject':'Good',
            'service_feedback':'Good Service',
        })
        self.assertTrue(form.is_valid())

    def test_feedback_form(self):
        form=FeedbackForm(data={})
      
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),3)   


    


