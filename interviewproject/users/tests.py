from django.test import TestCase
from .models import CustomUser

# user_controller response is :ok
# is_admin isn't returning json reponses

class usersTests(TestCase):
    def test_setup(self):
        CustomUser.objects.create(first_name = 'John', last_name = 'Smith', born_on = '1988-04-18')
        CustomUser.objects.create(first_name = 'Susan', last_name = 'Williams', born_on = '1972-08-03', is_admin = True)

    def test_ControllerResponse_ok(self):
        pass
    
    def test_JsonResponse_is_admin(self):
        pass



