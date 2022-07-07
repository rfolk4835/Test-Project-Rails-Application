from django.shortcuts import render
from django.http import JsonResponse
from .models import CustomUser
from django.db.models import Value as V
from django.db.models.functions import Concat  

# Start
# 'index' should return json response for each user, combining 'first_name' and 'last_name'
# exclude is_admin from the response

def Index(request):
    data = list(CustomUser.objects.annotate(full_name = Concat('first_name', V(' '), 'last_name')).exclude('is_admin','first_name','last_name'))
    return JsonResponse(data)

# Feature
# Support passing a parameter 'params[:search]' to query on 'last_name'

def Query_last_name(request):
    pass