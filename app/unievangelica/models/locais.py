from django.db import models
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError
# Create your models here.

class Bloco(models.Model):
    class Meta:
        verbose_name = "Bloco"
        verbose_name_plural = "Blocos"

    nome_bloco = models.CharField(
        max_length=20, 
        blank=False,
        verbose_name="Nome do bloco"
    )

    def __str__(self):
        return self.nome_bloco


class RecursoSala(models.Model):
    class Meta:
        verbose_name = 'Recurso da Sala'
        verbose_name_plural = 'Recursos da Sala'
    
    nome_recurso = models.CharField(
        max_length=128,
        verbose_name="Nome do Recurso"
        )

    def __str__(self):
        return self.nome_recurso



class Sala(models.Model):
    class Meta:
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'


    nome_sala = models.CharField(
        max_length=20,
        verbose_name="Nome da Sala",
        help_text="Informe o nome/identificação da sala"
    )
    bloco = models.ForeignKey(
        Bloco,
        on_delete=models.PROTECT,
    )
    quantidade_maxima = models.PositiveIntegerField(
        default=1,
        blank=False,
        verbose_name="Capacidade Máxima",
        help_text="Quantidade máxima de pessoas permitida na sala"
    )
    status = models.CharField(
        max_length=7,
        choices=(
        ('PUBLIC', 'Pública'),
        ('PRIVATE', 'Privada'),
        ),
        default='PUBLIC',
        help_text=mark_safe(
            'Privada: Indica que essa sala é restrita para um curso<br>'
            'Pública: Indica que essa sala é liberada para qualquer curso.'

        )
    )
    recursos_sala = models.ManyToManyField(
        RecursoSala, 
        verbose_name="Nome do Recurso"
        )

    curso = models.ForeignKey(
        'Cursos', 
        on_delete=models.PROTECT, 
        null=True,
        blank=True,
        verbose_name='Curso associado:',
        help_text='Opcional, caso a sala seja pública.'
        )
    
    def clean(self):
        if self.status == 'PRIVATE' and not self.curso:
            raise ValidationError(
                'Para uma sala ser privada, é necessário colocar a qual curso ela pertence.'
                )
        
        if self.quantidade_maxima < 1:
            raise ValidationError(
                'Quantidade de pessoas devem ser pelo menos 1.'
            )
        


    def __str__(self):
        return f'{self.nome_sala} ({self.bloco.nome_bloco})'

