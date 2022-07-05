from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .controllers import CustomUserController

# Start
# Intialized user with 4 variables
# Equivalent to 'database_design.sql'

class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    born_on = models.DateField()
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'first_name'
    REQUIRED_FIELDS = []

    objects = CustomUserController()

    def __str__(self):
        return self.first_name
