from django.db import models

# Create your models here.

class Bloco(models.Model):
    class Meta:
        verbose_name = "Bloco"
        verbose_name_plural = "Blocos"
        
    nome_bloco = models.CharField(max_length=20, blank=False)


class Sala(models.Model):
    class Meta:
        veborse_name = 'Sala'
        veborse_name_plural = 'Salas'
        unique_together = ['nome_sala', 'bloco']

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
    )
    # curso = models.ForeignKey('Curso', on_delete=models.SET_NULL, null=True)
    # recursos_sala = models.ForeignKey('RecursosSala', on_delete=models.CASCADE)
