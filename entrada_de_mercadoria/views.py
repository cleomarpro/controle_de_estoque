
from produto.models import EntradaMercadoria
from entrada_de_mercadoria.serializers import EntradaMercadoriaSerializer
#from usuarios.models import Usuarios
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
#from rest_framework.exceptions import NotFound
from django.contrib.auth.models import User
#from rest_framework.permissions import IsAuthenticated


                                                                                                
class EntradaMercadoriaCreate( APIView):
    def get(self, request):
        user = request.user.has_perm('produto.view_entradamercadoria')
        if user == False :
            return Response( status = status.HTTP_401_UNAUTHORIZED)
        user_logado = request.user # Obitendo o usuário logado
        user_logado = user_logado.id # obitendo o ID do usuário logado
        
        entradaMercadoria = EntradaMercadoria.objects.filter(user = user_logado)
        serializer = EntradaMercadoriaSerializer(entradaMercadoria, many = True)
        return Response(serializer.data)
        #return Response( status = status.HTTP_404_NOT_FOUND)

    def post(self, request):
        user_logado = request.user # Obitendo o usuário logado
        user_logado = user_logado.id # obitendo o ID do usuário logado
        user = request.user.has_perm('produto.add_entradamercadoria')
        if user == False :
            return Response( status = status.HTTP_401_UNAUTHORIZED)

        serializer = EntradaMercadoriaSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user = user_logado, usuarios_id = 1)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_404_BAD_CREATED)

class EntradaMercadoriaDetailChangeDelete(APIView):

    def get_object(self, pk):
        if EntradaMercadoria.objects.get(pk = pk):
            return EntradaMercadoria.objects.get(pk = pk)
        return Response( status = status.HTTP_404_NOT_FOUND)
        
    def get(self, request, pk):
        user = request.user.has_perm('produto.view_entradamercadoria')
        if user == False :
            return Response( status = status.HTTP_401_UNAUTHORIZED)
        user_logado = request.user 
        user_logado = user_logado.id 
        entrada_ercadoria = EntradaMercadoria.objects.filter(pk = pk, user = user_logado)
        if entrada_ercadoria:
            entradaMercadoria = self.get_object(pk)
            serializer = EntradaMercadoriaSerializer(entradaMercadoria)
            return Response(serializer.data)
        return Response( status = status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        user = request.user.has_perm('produto.change_entradamercadoria')
        if user == False :
            return Response( status = status.HTTP_401_UNAUTHORIZED)
        user_logado = request.user 
        user_logado = user_logado.id 
        entrada_ercadoria = EntradaMercadoria.objects.filter(pk = pk, user = user_logado)
        if entrada_ercadoria:
            entradaMercadoria = self.get_object(pk)
            serializer = EntradaMercadoriaSerializer(entradaMercadoria, data= request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        return Response( status = status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk):
        user = request.user.has_perm('produto.delete_entradamercadoria')
        if user == False :
            return Response( status = status.HTTP_401_UNAUTHORIZED)

        user_logado = request.user 
        user_logado = user_logado.id 
        entrada_ercadoria = EntradaMercadoria.objects.filter(pk = pk, user = user_logado)
        if entrada_ercadoria:
            entradaMercadoria = self.get_object(pk)
            entradaMercadoria.delete()
            return Response(status = status.HTTP_200_OK)
        return Response( status = status.HTTP_404_NOT_FOUND)




