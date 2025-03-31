from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
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
def api_get_bloco_detail(request, id):
    if request.method == "GET":
        bloco = Bloco.objects.filter(pk=id).first()
        serializer = SerializerBloco(
            instance=bloco, 
            many=False
            )
        return Response(serializer.data)
    
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
