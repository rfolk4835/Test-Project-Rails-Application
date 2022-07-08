from django.shortcuts import render
from django.http import JsonResponse
from .models import User
from django.db.models import Value as V
from django.db.models.functions import Concat

# Start
# 'index' should return json response for each user, combining 'first_name' and 'last_name'
# exclude is_admin from the response


def dict_map(v):
    full_name = "%s %s" % (v["first_name"], v["last_name"])
    return {"id": v["id"], "full_name": full_name, "born_on": v["born_on"]}


def index(request):
    queryset = User.objects.all()[0:100]
    data = list(queryset.values())
    data = [dict_map(v) for v in data]

    print(data)
    return JsonResponse({"users": data}, safe=False)
