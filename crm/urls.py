from django.urls import path
from django.conf.urls import handler404
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('clientes/create', views.cliente_create, name='create_cliente'),
]
