from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContatoInputSerializer
from .models import Contato


class CriarContatoView(APIView):
    def post(self, request):
        serializer = ContatoInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        Contato.objects.create(nome=data['nome'],
                               telefone=data['telefone'])
        return Response(status=status.HTTP_200_OK)
