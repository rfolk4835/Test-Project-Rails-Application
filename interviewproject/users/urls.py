from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path("", views.index, name="index"),
    path(".json?search=<str:last_name>", views.index, name="index")
]
