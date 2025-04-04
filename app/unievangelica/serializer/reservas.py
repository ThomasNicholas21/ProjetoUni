from rest_framework import serializers
from unievangelica.models import Cursos, Reservas, Sala
from django.contrib.auth.models import User
from datetime import timedelta
from dateutil.relativedelta import relativedelta

class SerializerUsuario(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'username', 'first_name', 'last_name', 'password'
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
            'id', 'nome_curso', 'coordenador', 'coordenador_objetos'
        ]
    
    coordenador = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        many=True,
    )
    coordenador_objetos = SerializerUsuario(
        source='coordenador', many=True, read_only=True
    )

    def validate_nome_curso(self, value):
        nome_curso = value

        if Cursos.objects.filter(nome_curso=nome_curso):
            raise serializers.ValidationError('Uma Sala com esse nome já existe.')

        return nome_curso
    

class SerializerReservas(serializers.ModelSerializer):
    class Meta:
        model = Reservas
        fields = [
            'id', 'nome_reserva', 'bloco', 'sala', 'data_reserva',
            'horario_inicio', 'horario_final',
            'coordenador', 'motivo_reserva',
            'curso', 'recorrencia', "quantidade_recorrencia",
        ]

    data_reserva = serializers.DateField(
        format="%d-%m-%Y",
        input_formats=[
            "%Y-%m-%d",
            "%d-%m-%Y",
            "%d/%m/%Y",
        ]
    )
    horario_inicio = serializers.TimeField(format="%H:%M")
    horario_final = serializers.TimeField(format="%H:%M")
    quantidade_recorrencia = serializers.IntegerField(
        required=False, 
        min_value=1, 
        default=1
    )

    def validate(self, attrs):
        data_reserva = attrs['data_reserva']
        horario_inicio = attrs['horario_inicio']
        horario_final = attrs['horario_final']
        sala = attrs['sala']
        curso = attrs['curso']

        if horario_inicio >= horario_final:
            raise serializers.ValidationError(
                'O horário inicial não deve ser maior que o final.'
            )
        
        if sala.status == 'PRIVATE' and curso != sala.curso:
            raise serializers.ValidationError(
                'A sala escolhida é privada e só pode ser reservada pelo curso associado.'
            )
        
        conflito = Reservas.objects.filter(
                        data_reserva=data_reserva,
                        sala=sala,
                    ).filter(
                        horario_inicio__lt=horario_final,
                        horario_final__gt=horario_inicio,
                    ).exists()

        if conflito:
            raise serializers.ValidationError(
                'Já existem reservas nesse horário, tente outro horário.'
            )
        
        return super().validate(attrs)

    
    def create(self, validated_data):
        recorrencia = validated_data.get("recorrencia", "N")
        quantidade = validated_data.pop("quantidade_recorrencia", 1)

        reserva_principal = Reservas.objects.create(**validated_data)

        if recorrencia == "N" or quantidade <= 1:
            return reserva_principal

        reservas = [reserva_principal]
        data_atual = validated_data["data_reserva"]
        nome_base = reserva_principal.nome_reserva

        intervalo = {
            "D": timedelta(days=1),
            "S": timedelta(weeks=1),
            "M": relativedelta(months=1),
        }.get(recorrencia)

        for i in range(1, quantidade):
            data_atual += intervalo
            nova_reserva_data = validated_data.copy()
            nova_reserva_data["data_reserva"] = data_atual
            nova_reserva_data["parent"] = reserva_principal
            nova_reserva_data["nome_reserva"] = f"{nome_base} - Recorrência {i}"

            reserva_recorrente = Reservas.objects.create(**nova_reserva_data)
            reservas.append(reserva_recorrente)

        reserva_principal.quantidade_recorrencia = quantidade
        reserva_principal.save(update_fields=["quantidade_recorrencia"])

        return reserva_principal


class SerializerDisponibilidadeReserva(serializers.Serializer):
    sala = serializers.PrimaryKeyRelatedField(queryset=Sala.objects.all())
    data_reserva = serializers.DateField(
        input_formats=["%Y-%m-%d", "%d-%m-%Y", "%d/%m/%Y"]
    )
    horario_inicio = serializers.TimeField(input_formats=["%H:%M", "%H:%M:%S"])
    horario_final = serializers.TimeField(input_formats=["%H:%M", "%H:%M:%S"])

    def validate(self, attrs):
        data_reserva = attrs['data_reserva']
        horario_inicio = attrs['horario_inicio']
        horario_final = attrs['horario_final']
        sala = attrs['sala']

        if horario_inicio >= horario_final:
            raise serializers.ValidationError(
                "O horário inicial deve ser menor que o horário final."
            )

        conflito = Reservas.objects.filter(
            sala=sala,
            data_reserva=data_reserva,
            horario_inicio__lt=horario_final,
            horario_final__gt=horario_inicio
        ).exists()

        if conflito:
            raise serializers.ValidationError(
                "Já existe uma reserva neste horário."
            )

        return attrs
        