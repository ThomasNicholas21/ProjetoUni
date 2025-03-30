from django.contrib import admin
from .models import Bloco, Sala, RecursoSala

# Register your models here.

@admin.register(Bloco)
class BlocoAdmin(admin.ModelAdmin):
    ...


@admin.register(RecursoSala)
class RecursoSalaAdmin(admin.ModelAdmin):
    ...


@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    ...
