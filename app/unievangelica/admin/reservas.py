from django.contrib import admin
from unievangelica.models import Cursos, Reservas

@admin.register(Cursos)
class AdminCursos(admin.ModelAdmin):
    list_display = ("id" ,"nome_curso",)
    search_fields = ("nome_curso",)
    autocomplete_fields = ("coordenador",)


@admin.register(Reservas)
class AdminReservas(admin.ModelAdmin):
    list_display = ("id" ,"nome_reserva", "sala", "data_reserva", "horario_inicio", "horario_final", "coordenador")
    list_filter = ("data_reserva", "sala", "coordenador")
    search_fields = ("nome_reserva", "coordenador__username", "sala__nome_sala")
    autocomplete_fields = ("bloco", "sala", "coordenador", "curso", "parent")
    fieldsets = (
        ("Detalhes da Reserva", {"fields": ("nome_reserva", "bloco", "sala", "data_reserva", "horario_inicio", "horario_final")}),
        ("Informações Adicionais", {"fields": ("coordenador", "motivo_reserva", "curso")}),
        ("Recorrência", {"fields": ("recorrencia", "quantidade_recorrencia", "parent")}),
    )
