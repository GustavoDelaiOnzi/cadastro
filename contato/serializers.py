from rest_framework import serializers

class ContatoInputSerializer(serializers.Serializer):
    nome = serializers.CharField()
    telefone = serializers.CharField()
    email = serializers.CharField(required=False)