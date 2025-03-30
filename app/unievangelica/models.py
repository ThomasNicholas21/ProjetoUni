from django.db import models

# Create your models here.

class Bloco(models.Model):
    class Meta:
        verbose_name = "Bloco"
        verbose_name_plural = "Blocos"

    nome_bloco = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.nome_bloco


class RecursoSala(models.Model):
    class Meta:
        verbose_name = 'Recurso da Sala'
        verbose_name_plural = 'Recursos da Sala'
    
    nome_recurso = models.CharField(max_length=128)

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
    )
    recursos_sala = models.ForeignKey(
        RecursoSala, 
        on_delete=models.CASCADE,
        null=True
        )

    # curso = models.ForeignKey('Curso', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.nome_sala} ({self.bloco.nome_bloco})'
