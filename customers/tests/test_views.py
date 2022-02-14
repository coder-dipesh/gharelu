from django.test import TestCase,Client
from django.urls import reverse


# Here we are testing the views ..
#  we test if views are rendering correct templates or not
# we get urls via reverse function and pass value to .assertTemplateUsed with expeted template with actual template

class Test_views(TestCase):
    def test_customerDashboard(self):
        client=Client()
        response=client.get(reverse('customers'))
        # self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'customers/customerDashboard.html')

    # def test_customerProfile(self):
    #     client=Client()
    #     response=client.get(reverse('customerprofile'))
    #     self.assertTemplateUsed(response,'customers/customerProfile.html')
      
    # def test_customerUpdateProfile(self):
    #     client=Client()
    #     response=client.get(reverse('customerupdateprofile'))
    #     self.assertTemplateUsed(response,'customers/customerUpdateProfile.html')
    
    # def test_myBookings(self):
    #     client=Client()
    #     response=client.get(reverse('my_bookings'))
    #     self.assertTemplateUsed(response,'customers/myBookings.html')

    # def test_feedbackForm(self):
    #     client=Client()
    #     response=client.get(reverse('feedback_form'))
    #     self.assertTemplateUsed(response,'customers/feedbackForm.html')