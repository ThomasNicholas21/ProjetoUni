from rest_framework import serializers
from unievangelica.models import Cursos


class SeralizerCursos(serializers.ModelSerializer):
    class Meta:
        model = Cursos
        fields = [
            'id', 'nome_curso', 'coordenador'
        ]
    
    coordenador = serializers.PrimaryKeyRelatedField(
        queryset=Cursos.objects.all(),
        many=True,
    )