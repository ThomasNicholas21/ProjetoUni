from django.db import models

# Create your models here.

class Bloco(models.Model):
    nome_bloco = models.CharField(max_length=20, blank=False)
    # sala = models.ForeignKey('Sala', on_delete=models.CASCADE)
