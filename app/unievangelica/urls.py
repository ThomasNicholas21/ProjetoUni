from django.urls import path
from .api import locais, reservas

urlpatterns = [
    # API user endpoints
    path('api/get/usuarios/', reservas.api_user, name='api_get_usuarios'),
    path('api/post/usuario/', reservas.api_user, name='api_post_usuario'),
    # API bloco endpoints
    path('api/get/blocos/', locais.api_get_blocos, name='api_get_blocos'),
    path('api/get/bloco/<int:id_bloco>/', locais.api_get_bloco_detail, name='apit_get_bloco_detail'),
    path('api/post/bloco/', locais.api_post_bloco, name='api_post_bloco'),
    # API recursos endpoints
    path('api/get/recursos_sala/', locais.api_get_recursos_sala, name='api_get_recursos_sala'),
    path('api/get/recurso_sala/<int:id_recurso>/', locais.api_get_recurso_sala_detail, name='apit_get_recurso_sala_detail'),
    path('api/post/recurso_sala/', locais.api_post_recurso_sala, name='api_post_bloco'),
    # API salas endpoints
    path('api/get/salas/', locais.api_get_salas, name='api_get_salas'),
    path('api/post/sala/', locais.api_post_sala, name='api_post_sala'),
    # API cursos endpoints
    path('api/get/cursos/', reservas.api_curso, name='api_get_cursos'),
    path('api/post/curso/', reservas.api_curso, name='api_post_curso'),
    # API reservas endpoints
    path('api/get/reservas/', reservas.api_reserva, name='api_get_reservas'),
    path('api/get/reserva/<int:id_reserva>', reservas.api_reserva_detail, name='api_get_reserva_detail'),
    path('api/post/reserva/', reservas.api_reserva, name='api_post_reservas'),


    # API Recurso Sala endpoints
    # API Sala endpoints
]
