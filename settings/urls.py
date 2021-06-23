
from django.contrib import admin
from django.urls import path
from api.views import users, customers

urlpatterns = [
    path('users/', users),
    path('customers/', customers),
]
