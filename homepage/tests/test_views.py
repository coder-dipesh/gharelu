from django.test import TestCase,Client
from django.urls import reverse


# Here we are testing the views ..
#  we test if views are rendering correct templates or not
# we get urls via reverse function and pass value to .assertTemplateUsed with expeted template with actual template

class Test_views(TestCase):
    def test_homepage(self):
        client=Client()
        response=client.get(reverse('homepage'))
        self.assertTemplateUsed(response,'homepage/homepage.html')
    
    def test_about(self):
        client=Client()
        response=client.get(reverse('about'))
        self.assertTemplateUsed(response,'homepage/about.html')

    def test_service(self):
        client=Client()
        response=client.get(reverse('service'))
        self.assertTemplateUsed(response,'homepage/service.html')

    def test_support(self):
        client=Client()
        response=client.get(reverse('support'))
        self.assertTemplateUsed(response,'homepage/support.html')