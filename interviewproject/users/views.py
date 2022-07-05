from django.shortcuts import render
from django.http import JsonResponse

# Start
# 'index' should return json response for each user, combining 'first_name' and 'last_name'
# exclude is_admin from the response

def index(request):
    pass

# Feature
# Support passing a parameter 'params[:search]' to query on 'last_name'