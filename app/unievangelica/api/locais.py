from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..serializer.locais import SerializerBloco, SerializerRecursoSala
from ..models.models_locais import Bloco, RecursoSala


# Bloco
@api_view(http_method_names=["get"])
def api_get_blocos(request):
    if request.method == "GET":
        blocos = Bloco.objects.all()
        serializer = SerializerBloco(
            instance=blocos, 
            many=True
            )
        return Response(serializer.data)
    
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(http_method_names=["get"])
def api_get_bloco_detail(request, id_bloco):
    if request.method == "GET":
        bloco = get_object_or_404(
            Bloco,
            pk=id_bloco
        )
        serializer = SerializerBloco(
            instance=bloco, 
            many=False
            )
        return Response(serializer.data)
    
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(http_method_names=['post'])
def api_post_bloco(request):
    if request.method == "POST":
        serializer = SerializerBloco(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)



# Recurso Sala
@api_view(http_method_names=["get"])
def api_get_recursos_sala(request):
    if request.method == "GET":
        recursos_sala = RecursoSala.objects.all()
        serializer = SerializerRecursoSala(
            instance=recursos_sala, 
            many=True
            )
        return Response(serializer.data)
    
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(http_method_names=["get"])
def api_get_recurso_sala_detail(request, id_recurso):
    if request.method == "GET":
        recurso_sala = get_object_or_404(RecursoSala, pk=id_recurso)
        serializer = SerializerRecursoSala(
            instance=recurso_sala, 
            many=False
            )
        return Response(serializer.data)
    
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(http_method_names=['post'])
def api_post_recurso_sala(request):
    if request.method == "POST":
        serializer = SerializerRecursoSala(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
