from django.contrib.auth.base_user import BaseUserManager

class CustomUserController(BaseUserManager):
    def CreateUser(self, first_name, last_name, born_on, is_admin):
        pass

    def CreateAdmin():
        pass



