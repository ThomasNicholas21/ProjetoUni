from rest_framework import serializers
from ..models.models_locais import Bloco
# construção dos serializers

class SerializerBloco(serializers.ModelSerializer):
    class Meta:
        model = Bloco
        fields = [
            "id", "nome_bloco"
        ]
