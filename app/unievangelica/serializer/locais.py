from rest_framework import serializers
from ..models.models_locais import Bloco
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
            raise serializers.ValidationError('')

        return nome_bloco
    