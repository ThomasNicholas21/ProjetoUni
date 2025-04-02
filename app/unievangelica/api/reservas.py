from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from ..models.reservas import Cursos, Reservas
from ..serializer.reservas import SerializerUsuario, SeralizerCursos, SerializerReservas


# Register User
@api_view(http_method_names=['get', 'post'])
def api_user(request):
    if request.method == 'GET':
        usuarios = User.objects.all()
        serializer = SerializerUsuario(
            instance=usuarios,
            many=True
        )
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SerializerUsuario(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


# Cursos
@api_view(http_method_names=['get', 'post'])
def api_curso(request):
    if request.method == 'GET':
        cursos = Cursos.objects.all()
        serializer = SeralizerCursos(
            instance=cursos,
            many=True
        )
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SeralizerCursos(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


# Reservas
@api_view(http_method_names=["get", "post"])
def api_reserva(request):
    if request.method == 'GET':
        reservas = Reservas.objects.all().order_by('id')
        serializer = SerializerReservas(
            instance=reservas, 
            many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = SerializerReservas(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(http_method_names=["get", "delete"])
def api_reserva_detail(request, id_reserva):
    if request.method == 'GET':
        reserva = get_object_or_404(
            Reservas, pk=id_reserva
        )
        serializer = SerializerReservas(
            instance=reserva, 
            many=False)
        return Response(serializer.data)

    elif request.method == "DELETE":
        serializer = SerializerReservas(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
