from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path("query/<str:last_name>", views.query, name="query"),
    path("index/", views.index, name="index"),
]
