from django.test import TestCase,Client
from django.urls import reverse


# Here we are testing the views ..
#  we test if views are rendering correct templates or not
# we get urls via reverse function and pass value to .assertTemplateUsed with expeted template with actual template

class Test_views(TestCase):
    def test_professionalDashboard(self):
        client=Client()
        response=client.get(reverse('professionals'))
        self.assertTemplateUsed(response,'professionals/professionalDashboard.html')
    
        
    def test_service(self):
        client=Client()
        response=client.get(reverse('services'))
        self.assertTemplateUsed(response,'professionals/service.html')


    def test_bookings(self):
        client=Client()
        response=client.get(reverse('bookings'))
        self.assertTemplateUsed(response,'professionals/bookings.html')

    def test_changePassword(self):
        client=Client()
        response=client.get(reverse('change_password'))
        self.assertTemplateUsed(response,'professionals/changePassword.html')
    
    def test_service_form(self):
        client=Client()
        response=client.get(reverse('service_form'))
        self.assertTemplateUsed(response,'professionals/service_form.html')
    