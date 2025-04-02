from django.urls import path
from .api import locais, reservas
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

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
    path('api/post/recurso_sala/', locais.api_post_recurso_sala, name='api_post_recurso_sala'),
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
    path('api/delete/reserva/<int:id_reserva>', reservas.api_reserva_detail, name='api_delete_reserva_detail'),
    # API disponibilidade endpoint
    path('api/post/reserva/disponibilidade/', reservas.api_reserva_disponivel, name='api_reserva_disponivel'),
    # API relatorios endpoint
    path('api/get/relatorio/', reservas.api_get_relatorios, name='api_get_relatorio'),
    # API JWT
    path('api/user/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
