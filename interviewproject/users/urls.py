from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name = 'index'),
    path('', views.Query_last_name, name = 'query_last_name'),
]