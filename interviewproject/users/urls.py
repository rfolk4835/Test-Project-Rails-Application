from django.urls import path
from . import views

urlpatterns = [
    path('users/index', views.Index, name = 'index'),
    path('users/query/<str:last_name_prefix>', views.Query_last_name_Prefix, name = 'query_last_name_prefix'),
]