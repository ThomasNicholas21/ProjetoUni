from django.contrib import admin
from unievangelica.models import Bloco, Sala, RecursoSala

# Register your models here.

@admin.register(Bloco)
class BlocoAdmin(admin.ModelAdmin):
    list_display = ("id" ,"nome_bloco",)
    search_fields = ("nome_bloco",)


@admin.register(RecursoSala)
class RecursoSalaAdmin(admin.ModelAdmin):
    list_display = ("id" ,"nome_recurso",)
    search_fields = ("nome_recurso",)


@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ("id" ,"nome_sala", "bloco", "quantidade_maxima", "status")
    list_filter = ("bloco", "status")
    search_fields = ("nome_sala",)
    autocomplete_fields = ("recursos_sala", "curso")
    fieldsets = (
        ("Informações Gerais", {"fields": ("nome_sala", "bloco", "quantidade_maxima", "status")}),
        ("Recursos e Curso", {"fields": ("recursos_sala", "curso")}),
    )

