from datetime import timedelta
from unievangelica.models import Reservas, Sala 
from django.db.models import Count

def gerar_relatorio():
    salas_mais_reservadas = Reservas.objects.values(
        'sala__nome_sala', 
        'sala__bloco__nome_bloco'
    ).annotate(
        total_reservas=Count('id')
    ).order_by('-total_reservas')[:5]

    horarios_pico = Reservas.objects.values(
        'horario_inicio'
    ).annotate(
        total=Count('id')
    ).order_by('-total')[:5]

    salas = Sala.objects.all()
    taxa_ocupacao_salas = []

    for sala in salas:
        reservas = Reservas.objects.filter(sala=sala)
        
        if not reservas.exists():
            taxa_ocupacao_salas.append({
                "sala": sala.nome_sala,
                "bloco": sala.bloco.nome_bloco,
                "taxa_ocupacao": "0.00%"
            })
            continue
        
        primeiro_dia = reservas.earliest('data_reserva').data_reserva
        ultimo_dia = reservas.latest('data_reserva').data_reserva
        total_dias = (ultimo_dia - primeiro_dia).days + 1

        total_horas_reservadas = 0
        for reserva in reservas:
            inicio = reserva.horario_inicio
            fim = reserva.horario_final
            
            diferenca = timedelta(
                hours=fim.hour - inicio.hour,
                minutes=fim.minute - inicio.minute
            )
            total_horas_reservadas += diferenca.total_seconds() / 3600
        
        total_horas_disponiveis = total_dias * 24

        if total_horas_disponiveis > 0:
            taxa_ocupacao = (total_horas_reservadas / total_horas_disponiveis) * 100
        else:
            taxa_ocupacao = 0
        
        taxa_ocupacao_salas.append({
            "sala": sala.nome_sala,
            "bloco": sala.bloco.nome_bloco,
            "taxa_ocupacao": f"{taxa_ocupacao:.2f}%"
        })
    
    relatorio = {
        "salas_mais_reservadas": list(salas_mais_reservadas),
        "horarios_pico": list(horarios_pico),
        "taxa_ocupacao_salas": taxa_ocupacao_salas
    }
    
    return relatorio
