from django.db import models

class Trilha(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    

    def __str__(self):
        return self.titulo

class Etapa(models.Model):
    trilha = models.ForeignKey(Trilha, related_name='etapas', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    assistido = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"Etapa {self.id}: {self.titulo} em {self.trilha.titulo}"
    
class Ligacao(models.Model):
    etapa = models.ForeignKey(Etapa, related_name='ligacoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    duracao = models.IntegerField(help_text="Duração em minutos")

class Link(models.Model):
    etapa = models.ForeignKey(Etapa, related_name='links', on_delete=models.CASCADE)
    url = models.URLField()
    nome = models.CharField(max_length=200)