from rest_framework import serializers
from unievangelica.models import Cursos
from django.contrib.auth.models import User


class SerializerUsuario(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'password'
        ]
        extra_kwargs = {'password': {'write_only': True}}
    
    def validate(self, attrs):
        required_fields = ['username', 'first_name', 'last_name', 'password']
        
        for field in required_fields:
            if not attrs.get(field):
                raise serializers.ValidationError(f'O campo {field} é obrigatório.')
        
        return super().validate(attrs)


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