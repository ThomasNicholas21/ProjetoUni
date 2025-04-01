from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
import calendar

# Create your models here.


class Cursos(models.Model):
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    nome_curso = models.CharField(max_length=128, verbose_name='Nome do Curso:')
    coordenador = models.ManyToManyField(User)

    def __str__(self):
        return self.nome_curso


class Reservas(models.Model):
    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ['data_inicio']
    
    # Tipos de recorrência
    RECORRENCIA_CHOICES = [
        ('NENHUMA', 'Nenhuma recorrência'),
        ('DIARIA', 'Diária'),
        ('SEMANAL', 'Semanal'),
        ('MENSAL', 'Mensal'),
    ]
    
    bloco = models.ForeignKey('Bloco', on_delete=models.PROTECT)
    sala = models.ForeignKey('Sala', on_delete=models.PROTECT)
    data_inicio = models.DateTimeField()
    data_final = models.DateTimeField()
    coordenador = models.ForeignKey(User, on_delete=models.PROTECT)
    motivo_reserva = models.TextField()
    curso = models.ForeignKey('Cursos', on_delete=models.PROTECT, null=True, blank=True)
    recorrencia = models.CharField(
        max_length=10,
        choices=(
        ('NENHUMA', 'Nenhuma recorrência'),
        ('DIARIA', 'Diária'),
        ('SEMANAL', 'Semanal'),
        ('MENSAL', 'Mensal'),
        ),
        default='NENHUMA',
        verbose_name='Tipo de recorrência'
    )
    recorrencia_fim = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Data final da recorrência'
    )
    dias_recorrencia = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text='Para recorrência semanal, informe os dias (ex: 2,4 para terça e quinta)'
    )

    def __str__(self):
        return f"Reserva {self.sala} - {self.data_inicio.strftime('%d/%m/%Y %H:%M')}"
    
    def clean(self):
        if self.data_inicio >= self.data_final:
            raise ValidationError("A data final deve ser após a data de início")
            
        if self.recorrencia != 'NENHUMA' and not self.recorrencia_fim:
            raise ValidationError("Para reservas recorrentes, informe a data final da recorrência")
        
        if self.sala.status == 'PRIVATE' and self.curso != self.sala.curso:
            raise ValidationError("Esta sala é privada e só pode ser reservada pelo curso proprietário")

    @property
    def ocorrencias_da_recorrencia(self):
        if self.recorrencia == 'NENHUMA':
            return [(self.data_inicio, self.data_final)]
            
        ocorrencias = []
        
        while self.data_inicio <= self.recorrencia_fim:
            ocorrencias.append((self.data_inicio, self.data_final))
            
            if self.recorrencia == 'DIARIA':
                self.data_inicio += timezone.timedelta(days=1)
                self.data_final += timezone.timedelta(days=1)

            elif self.recorrencia == 'SEMANAL':
                self.data_inicio += timezone.timedelta(weeks=1)
                self.data_final += timezone.timedelta(weeks=1)

            elif self.recorrencia == 'MENSAL':
                try:
                    self.data_inicio = self.data_inicio.replace(month=self.data_inicio.month + 1)
                    self.data_final = self.data_final.replace(month=self.data_final.month + 1)
                    
                except ValueError:
                    if self.data_inicio.month == 12:
                        self.data_inicio = self.data_inicio.replace(year=self.data_inicio.year + 1, month=1)
                        self.data_final = self.data_final.replace(year=self.data_final.year + 1, month=1)

                    else:
                        proximo_mes = self.data_inicio.month + 1
                        proximo_ano = self.data_inicio.year
                        
                        if proximo_mes > 12:
                            proximo_mes = 1
                            proximo_ano += 1
                        
                        ultimo_dia_original = calendar.monthrange(self.data_inicio.year, self.data_inicio.month)[1]

                        if self.data_inicio.day == ultimo_dia_original:
                            ultimo_dia_proximo = calendar.monthrange(proximo_ano, proximo_mes)[1]
                            self.data_inicio = self.data_inicio.replace(year=proximo_ano, month=proximo_mes, day=ultimo_dia_proximo)
                            self.data_final = self.data_final.replace(year=proximo_ano, month=proximo_mes, day=ultimo_dia_proximo)

                        else:
                            try:
                                self.data_inicio = self.data_inicio.replace(year=proximo_ano, month=proximo_mes)
                                self.data_final = self.data_final.replace(year=proximo_ano, month=proximo_mes)

                            except ValueError:
                                ultimo_dia_proximo = calendar.monthrange(proximo_ano, proximo_mes)[1]
                                self.data_inicio = self.data_inicio.replace(year=proximo_ano, month=proximo_mes, day=ultimo_dia_proximo)
                                self.data_final = self.data_final.replace(year=proximo_ano, month=proximo_mes, day=ultimo_dia_proximo)

        return ocorrencias
    