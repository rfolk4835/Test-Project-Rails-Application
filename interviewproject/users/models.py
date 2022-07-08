from django.db import models

# Start
# Intialized user with 4 variables
# Equivalent to 'database_design.sql'

class CustomUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    born_on = models.DateField()
    is_admin = models.BooleanField(default=False)

    objects = models.Manager

    def __str__(self):
        return self.first_name + ' ' + self.last_name



