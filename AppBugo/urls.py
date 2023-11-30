from django.urls import path
from .views import categorias, productos, clientes


urlpatterns = [
    path('categoria/', categorias, name='categoria'),
    path('producto/', productos, name='producto'),
    path('cliente/', clientes, name='cliente'),
]
