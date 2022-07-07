from django.shortcuts import render
from django.http import JsonResponse
from .models import CustomUser

# Start
# 'index' should return json response for each user, combining 'first_name' and 'last_name'
# exclude is_admin from the response

def Index(request):
    data = list(CustomUser.objects.values())
    return JsonResponse(data, safe = False)

# Feature
# Support passing a parameter 'params[:search]' to query on 'last_name'

def Query_last_name(request):
    pass