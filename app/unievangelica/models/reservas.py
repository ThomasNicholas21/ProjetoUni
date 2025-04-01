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
