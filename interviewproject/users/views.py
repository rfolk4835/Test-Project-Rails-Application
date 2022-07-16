from django.http import JsonResponse
from .models import User

# Start
# 'index' should return json response for each user, combining 'first_name' and 'last_name'
# exclude is_admin from the response

# Feature 
# Support passing in a parameter when a parameter is present in 'index'
# Filter by last_name using a begins with search


def dict_map(v):
    full_name = "%s %s" % (v["first_name"], v["last_name"])
    return {"id": v["id"], "full_name": full_name, "born_on": v["born_on"]}


def index(request, name_query):
    queryset = User.objects.all()[0:100]
    if (not name_query):
        nameset = queryset.filter(last_name__startswith = name_query)
        data = list(nameset.values())
    else:
        data = list(queryset.values())

    data = [dict_map(v) for v in data]
    print(data)
    return JsonResponse({"users": data}, safe=False)
