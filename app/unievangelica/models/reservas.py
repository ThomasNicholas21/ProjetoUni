from django.db import models
from django.contrib.auth.models import User


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
    
    nome_reserva = models.CharField(max_length=128, default='')
    bloco = models.ForeignKey(
        'Bloco', on_delete=models.PROTECT
    )
    sala = models.ForeignKey(
        'Sala', on_delete=models.PROTECT
    )
    data_reserva = models.DateField()
    horario_inicio = models.TimeField()
    horario_final = models.TimeField()
    coordenador = models.ForeignKey(
        User, on_delete=models.PROTECT
    )
    motivo_reserva = models.TextField()
    curso = models.ForeignKey(
        'Cursos', 
        on_delete=models.PROTECT, 
        null=True, blank=True
    )
    recorrencia = models.CharField(
        choices=(
            ("N", "Sem recorrência"),
            ("D", "Diária"),
            ("S", "Semanal"),
            ("M", "Mensal"),
        ),
        default="N",
    )
    quantidade_recorrencia = models.PositiveIntegerField(
        null=True, blank=True
    )
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="recorrencias"
    )

    def __str__(self):
        return f'{self.nome_reserva} para {self.curso.nome_curso} feito por {self.coordenador.first_name}'

