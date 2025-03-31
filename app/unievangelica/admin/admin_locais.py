from django.contrib import admin
from unievangelica.models import Bloco, Sala, RecursoSala

# Register your models here.

@admin.register(Bloco)
class BlocoAdmin(admin.ModelAdmin):
    ...


@admin.register(RecursoSala)
class RecursoSalaAdmin(admin.ModelAdmin):
    search_fields = 'nome_recurso',


@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    autocomplete_fields = 'recursos_sala',
    search_fields = 'nome_sala',

