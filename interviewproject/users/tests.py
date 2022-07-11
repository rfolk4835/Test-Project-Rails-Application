
from urllib import response
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

    def test_JsonResponse_Index(self):
        test_data = {"id": 1, "full_name": "John Smith", "born_on": "1980-03-12"}
        response = client.post(path = "users/", data = test_data) 

    def test_JsonResponse_Query(self):
        pass
