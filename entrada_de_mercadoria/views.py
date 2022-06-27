from ast import Return
from produto.models import EntradaMercadoria
from entrada_de_mercadoria.serializers import EntradaMercadoriaSerializer
from usuarios.models import Usuarios
from django.shortcuts import redirect
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework import permissions, authentication


  
class EntradaMercadoriaCreate(APIView):
    def get(self, request):
        permission_classes = [permissions.IsAuthenticated]
        authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
        if permission_classes and authentication_classes:
            entradaMercadoria = EntradaMercadoria.objects.all()
            serializer = EntradaMercadoriaSerializer(entradaMercadoria, many = True)
            return Response(serializer.data)

    def post(self, request):
        serializer = EntradaMercadoriaSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_404_BAD_CREATED)

class EntradaMercadoriaDetailChengeDelite(APIView):
    def get_object(self, pk):
        try:
            return EntradaMercadoria.objects.get(pk = pk)
        except EntradaMercadoria.DoesNotExist:
            return NotFound()

    def get(self, request, pk):
        entradaMercadoria = self.get_object(pk)
        serializer = EntradaMercadoriaSerializer(entradaMercadoria)
        return Response(serializer.data)

    def put(self, request, pk):
        entradaMercadoria = self.get_object(pk)
        serializer = EntradaMercadoriaSerializer(entradaMercadoria, data= request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        entradaMercadoria = self.get_object(pk)
        entradaMercadoria.delete()
        return Response(status = status.HTTP_200_OK)




