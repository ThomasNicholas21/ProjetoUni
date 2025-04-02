import logging
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from unievangelica.models import Reservas

logger = logging.getLogger('notificacoes')

class Command(BaseCommand):
    help = "Simula envio de notificações sobre reservas futuras"

    def handle(self, *args, **kwargs):
        hoje = datetime.now().date()
        proximos_dias = hoje + timedelta(days=2)

        reservas = Reservas.objects.filter(data_reserva__range=[hoje, proximos_dias])

        if reservas.exists():
            for reserva in reservas:
                mensagem = f"Reserva para {reserva.sala.nome_sala} no dia {reserva.data_reserva} das {reserva.horario_inicio} às {reserva.horario_final}."
                logger.info(mensagem)
                print(mensagem)  # Apenas para testes (mensagens estão disponíveis na pasta log)
        else:
            logger.info("Nenhuma reserva próxima para notificar.")
