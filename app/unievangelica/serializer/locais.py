from rest_framework import serializers
from ..models.models_locais import Bloco, RecursoSala, Sala
# construção dos serializers

class SerializerBloco(serializers.ModelSerializer):
    class Meta:
        model = Bloco
        fields = [
            "id", "nome_bloco"
        ]
    
    def validate_nome_bloco(self, value):
        nome_bloco = value

        if Bloco.objects.filter(nome_bloco=nome_bloco):
            raise serializers.ValidationError('Um bloco com esse nome já existe.')

        return 


class SerializerRecursoSala(serializers.ModelSerializer):
    class Meta:
        model = RecursoSala
        fields = [
            "id", "nome_recurso"
        ]
    
    def validate_nome_recurso(self, value):
        nome_recurso = value

        if RecursoSala.objects.filter(nome_recurso=nome_recurso):
            raise serializers.ValidationError('Um recurso com esse nome já existe.')

        return nome_recurso
    

class SerializerSala(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = [
            "id", "nome_sala", "bloco",
            "quantidade_maxima", "status",
            "recursos_sala",
        ]
    
    recursos_sala = serializers.PrimaryKeyRelatedField(
        queryset=RecursoSala.objects.all(),
        many=True,
    )
    

    
    