from django.db import models
from models.users import Users
import json

# Start
# 'index' should return json response for each user, combining 'first_name' and 'last_name'
# exclude is_admin from the response

def __init__(self, first_name = None, last_name = None, born_on = '01/01/1901', is_admin = False):
    self.first_name = first_name
    self.last_name = last_name
    self.born_on = born_on
    self.is_admin = is_admin

# def index(self):
    

# Feature
# Support passing a parameter 'params[:search]' to query on 'last_name'



