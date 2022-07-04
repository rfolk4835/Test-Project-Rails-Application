from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

# Start
# Intialized user with 4 variables
# Equivalent to 'database_design.sql'

# AUTH_USER_MODEL = 'models.users'

class Users(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    born_on = models.DateField()
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'first_name' + 'last_name'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.USERNAME_FIELD