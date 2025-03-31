from django.urls import path
from .api import locais

urlpatterns = [
    # API bloco endpoints
    path('api/get/blocos/', locais.api_get_blocos, name='api_get_blocos'),
    path('api/get/bloco/<int:id_bloco>/', locais.api_get_bloco_detail, name='apit_get_bloco_detail'),
    path('api/post/bloco/', locais.api_post_bloco, name='api_post_bloco'),
    # API recursos endpoints
    path('api/get/recursos_sala/', locais.api_get_recursos_sala, name='api_get_recursos_sala'),
    path('api/get/bloco/<int:id_bloco>/', locais.api_get_bloco_detail, name='apit_get_bloco_detail'),



    # API Recurso Sala endpoints
    # API Sala endpoints
]
