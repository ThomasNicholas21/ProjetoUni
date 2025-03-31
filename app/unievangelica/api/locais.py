from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..serializer.locais import SerializerBloco
from ..models.models_locais import Bloco


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
