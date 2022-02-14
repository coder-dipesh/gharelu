from django.test import TestCase,Client
from django.urls import reverse


# Here we are testing the views ..
#  we test if views are rendering correct templates or not
# we get urls via reverse function and pass value to .assertTemplateUsed with expeted template with actual template

class Test_views(TestCase):
    def test_adminDashboard_get(self):
        client=Client()
        response=client.get(reverse('admins'))
        # self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'admins/adminDashboard.html')

    def test_get_feedback_get(self):
        client=Client()
        response=client.get(reverse('get_feedback'))
        self.assertTemplateUsed(response,'admins/get_feedback.html')

    def test_get_allservices_get(self):
        client=Client()
        response=client.get(reverse('get_allservices'))
        self.assertTemplateUsed(response,'admins/get_service.html')
    
    def test_get_allorders_get(self):
        client=Client()
        response=client.get(reverse('get_allorders'))
        self.assertTemplateUsed(response,'admins/get_order.html')

    def test_allCategory_get(self):
        client=Client()
        response=client.get(reverse('category'))
        self.assertTemplateUsed(response,'admins/category.html')

    def test_category_form_get(self):
        client=Client()
        response=client.get(reverse('category_form'))
        self.assertTemplateUsed(response,'admins/category_form.html')

    def  test_allAdmins(self):
        client=Client()
        response=client.get(reverse('alladmins'))
        self.assertTemplateUsed(response,'admins/allAdmins.html')

    