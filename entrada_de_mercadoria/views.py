
from produto.models import EntradaMercadoria
from entrada_de_mercadoria.serializers import EntradaMercadoriaSerializer
#from usuarios.models import Usuarios
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
#from rest_framework.exceptions import NotFound
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
#from rest_framework import permissions, authentication


                                                                                                
class EntradaMercadoriaCreate( APIView):
    permission_classes = (IsAuthenticated,)
    #permission_classes = [permissions.IsAuthenticated]
    #authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

    #def get_queryset(self):
        #user = self.request.user
        #return List.objects.filter(owner=user)
        
    def get(self, request):
        entradaMercadoria = EntradaMercadoria.objects.all()
        serializer = EntradaMercadoriaSerializer(entradaMercadoria, many = True)
        return Response(serializer.data)
        #return Response( status = status.HTTP_404_NOT_FOUND)

    def post(self, request):
       
        serializer = EntradaMercadoriaSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_404_BAD_CREATED)

class EntradaMercadoriaDetailChangeDelete(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        return EntradaMercadoria.objects.get(pk = pk)
       
    def get(self, request, pk):
        try:
            entradaMercadoria = self.get_object(pk)
            serializer = EntradaMercadoriaSerializer(entradaMercadoria)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

    def put(self, request, pk): 
        try:
            entradaMercadoria = self.get_object(pk)
            serializer = EntradaMercadoriaSerializer(entradaMercadoria, data= request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk):
        try:
            entradaMercadoria = self.get_object(pk)
            entradaMercadoria.delete()
            return Response(status = status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)




