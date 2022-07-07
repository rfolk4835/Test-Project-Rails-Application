from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name = 'index'),
    path('users/<str:last_name_prefix>', views.Query_last_name_Prefix, name = 'query_last_name_prefix'),
]