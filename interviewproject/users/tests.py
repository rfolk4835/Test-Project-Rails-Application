from django.test import TestCase, Client
from django.urls import reverse

client = Client()

# user_controller response is :ok
# is_admin isn't returning json reponses


class usersTests(TestCase):
    def test_ControllerResponse(self):
        response = client.get(reverse("users:index"))
        self.assertEqual(response.status_code, 200)
