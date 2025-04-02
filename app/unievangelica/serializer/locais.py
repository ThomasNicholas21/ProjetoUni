from rest_framework import serializers
from ..models import Bloco, RecursoSala, Sala, Cursos
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

        return value


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
            "recursos_sala", 'recursos_sala_objetos', 'curso'
        ]
    
    recursos_sala = serializers.PrimaryKeyRelatedField(
        queryset=RecursoSala.objects.all(),
        many=True,
    )
    recursos_sala_objetos = SerializerRecursoSala(
        source='recursos_sala', many=True, read_only=True
    )
    
    def validate_nome_sala(self, value):
        nome_sala = value

        if Sala.objects.filter(nome_sala=nome_sala):
            raise serializers.ValidationError('Uma Sala com esse nome já existe.')

        return nome_sala
    
    def validate(self, attrs):
        status = attrs.get('status')
        curso = attrs.get('curso')
        quantidade_maxima = attrs.get('quantidade_maxima')
        
        if status == 'PRIVATE' and not curso:
            raise serializers.ValidationError(
                'Uma sala privada deve estar associada a um curso.'
            )
        
        if quantidade_maxima <= 0:
            raise serializers.ValidationError(
                'Sala deve ter ao menos 1 de capacidade máxima.'
            )
            
        
        return super().validate(attrs)
    