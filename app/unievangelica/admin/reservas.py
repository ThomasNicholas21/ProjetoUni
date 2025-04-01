from django.contrib import admin
from unievangelica.models import Cursos, Reservas

@admin.register(Cursos)
class AdminCursos(admin.ModelAdmin):
    autocomplete_fields = 'coordenador',
    search_fields = 'nome_curso',


@admin.register(Reservas)
class AdminReservas(admin.ModelAdmin):
    ...
