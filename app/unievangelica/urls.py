from django.urls import path
from .api import locais

urlpatterns = [
    # API bloco endpoints
    path('api/get/blocos/', locais.api_get_blocos, name='api_get_blocos'),
    path('api/get/bloco/<int:id>/', locais.api_get_bloco_detail, name='apit_get_bloco_detail'),
    # path('api/bloco', locais.teste, name='bloco'),
    # path('api/bloco', locais.teste, name='bloco'),

    # API Recurso Sala endpoints
    # API Sala endpoints
]
