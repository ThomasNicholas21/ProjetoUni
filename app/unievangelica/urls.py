from django.urls import path
from .api import locais

urlpatterns = [
    # API bloco endpoints
    path('api/get/blocos/', locais.api_get_blocos, name='api_get_blocos'),
    # path('api/bloco', locais.teste, name='bloco'),
    # path('api/bloco', locais.teste, name='bloco'),
    # path('api/bloco', locais.teste, name='bloco'),

    # API Recurso Sala endpoints
    # API Sala endpoints
]
