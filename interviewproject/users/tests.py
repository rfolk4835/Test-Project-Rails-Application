
from django.test import TestCase, Client
from django.urls import reverse

client = Client()

# Wrap Up
# test user controller response is ok. 
# test is_admin isn't returning json reponses. 

class usersTests(TestCase):
    def test_ControllerResponse(self):
        response = client.get(reverse("users:index"))
        self.assertEqual(response.status_code, 200)
