from rest_framework.decorators import api_view
from rest_framework.response import Response
from auctions.models import Listing,Category
from .serializers import IhaSerializer
from rest_framework import status

@api_view(['GET'])
def getRoutes(request):
    routes = {
        "GET All ihas": "/api/ihas/",
        "GET ihas by ID": "/api/ihas/<int:pk>/",
        "CREATE New ihas": "/api/ihas/create/",
        "UPDATE ihas by ID": "/api/ihas/<int:pk>/update/",
        "DELETE ihas by ID": "/api/ihas/<int:pk>/delete/",
    }
    return Response(routes)

@api_view(['GET'])
def getIhas(request):
    ihas=Listing.objects.all()
    serializer = IhaSerializer(ihas , many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getIha(request, pk):
    iha=Listing.objects.get(id=pk)
    serializer = IhaSerializer(iha , many=False)
    return Response(serializer.data)

@api_view(['PUT', 'PATCH'])
def updateIha(request, pk):
    try:
        iha = Listing.objects.get(id=pk)
    except Listing.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT' or request.method == 'PATCH':
        serializer = IhaSerializer(instance=iha, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteIha(request, pk):
    try:
        iha = Listing.objects.get(id=pk)
    except Listing.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    iha.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)