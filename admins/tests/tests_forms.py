from django.test import SimpleTestCase
from admins.forms import  *


class TestForms(SimpleTestCase):
    def test_category_form(self):
        form=CategoryForm(data={
            'category_name':'Mechanic',
            'category_description':"Hello! I am mechanic and I fix mechanical issues",
        })
        self.assertTrue(form.is_valid())

    def test_category_form(self):
        form=CategoryForm(data={})
      
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),2)


    


