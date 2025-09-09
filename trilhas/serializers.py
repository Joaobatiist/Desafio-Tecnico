from rest_framework import serializers
from .models import Trilha, Etapa, Ligacao, Link


class LigacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ligacao
        fields = [ 'nome', 'telefone', 'duracao']

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = [ 'url', 'nome']

class EtapaSerializer(serializers.ModelSerializer):
    ligacoes = LigacaoSerializer(many=True, read_only=True)
    links = LinkSerializer(many=True, read_only=True)

    class Meta:
        model = Etapa
        fields = ['id', 'trilha', 'titulo', 'descricao', 'assistido', 'ligacoes', 'links']
        extra_kwargs = {
            'trilha': {'write_only': True}
        }

class TrilhaSerializer(serializers.ModelSerializer):
    etapas = EtapaSerializer(many=True, read_only=True)

    class Meta:
        model = Trilha
        fields = ['id', 'titulo', 'descricao', 'etapas']
         
        