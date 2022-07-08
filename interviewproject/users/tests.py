from click import password_option
from django.test import TestCase
from .models import CustomUser
from django.urls import reverse


# Wrap Up
# test user controller response is ok. 
# test is_admin isn't returning json reponses. 

class usersTests(TestCase):
    def setupTestData(self):
        CustomUser.objects.create(first_name = 'John', last_name = 'Wilson', born_on = '1988-04-18')
        CustomUser.objects.create(first_name = 'Susan', last_name = 'Williams', born_on = '1972-08-03', is_admin = True)

    def test_ControllerResponse(self):
        response = self.client.get('users/')
        self.assertEqual(response.status_code, 200)

    def test_JsonResponse_Index(self):
        response = self.client.get('users/index')

    def test_JsonResponse_Query(self):
        response = self.client.get('users/query/Wil')



