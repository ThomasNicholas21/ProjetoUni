from rest_framework import serializers
from unievangelica.models import Cursos
from django.contrib.auth.models import User


class SerializerUsuario(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password'
        ]
        extra_kwargs = {'password': {'write_only': True}}


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