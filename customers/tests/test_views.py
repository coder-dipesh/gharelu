from django.test import TestCase,Client
from django.urls import reverse


# Here we are testing the views ..
#  we test if views are rendering correct templates or not
# we get urls via reverse function and pass value to .assertTemplateUsed with expeted template with actual template

class Test_views(TestCase):
    def test_customerDashboard(self):
        client=Client()
        response=client.get(reverse('customers'))
        self.assertTemplateUsed(response,'customers/customerDashboard.html')

