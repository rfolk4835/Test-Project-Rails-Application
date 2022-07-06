from django.contrib.auth.base_user import BaseUserManager

class CustomUserController(BaseUserManager):
    def CreateUser(self, username, password, first_name, last_name, born_on, **extrafields):
        user = self.model(username = username, first_name = first_name, 
                            last_name = last_name, born_on = born_on, **extrafields)
        user.set_password(password)
        user.save()
        
        return user

    def CreateAdmin(self, username, password, first_name, last_name, born_on, **extrafields):
        extrafields.setdefault('is_admin', True)
        extrafields.setdefault('is_superuser', True)

        return self.CreateUser(username, password, first_name, last_name, born_on, **extrafields)



