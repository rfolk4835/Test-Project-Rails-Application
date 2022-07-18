
from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from sqlalchemy import true
from .models import User

client = Client()

# Wrap Up
# test user controller response is ok. 
# test is_admin isn't returning json reponses. 

class usersTests(TestCase):
    def test_ControllerResponse(self):
        response = client.get(reverse("users:index"))
        self.assertEqual(response.status_code, 200)

    def test_JsonResponse_Index(self):
        self.user = User.objects.create(first_name = "John", last_name = "Smith", born_on = "1980-05-01", is_admin = True)
        check = b"is_admin"
        response = client.get(reverse("users:index"))
        self.assertNotIn(check, response.json())

    def test_JsonResponse_Query(self):
        self.user = User.objects.create(first_name = "John", last_name = "Smith", born_on = "1980-05-01", is_admin = True)
        check = b"is_admin"
        response = client.get(reverse("users:query", args = ["Smith"]))
        self.assertNotIn(check, response.json())