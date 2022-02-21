from turtle import title
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here. esse

class Chamado_geral(models.Model):

    STATUS = (
        ('Solicitado', 'Solicitado'),       # Solicitado
        ('Em_andamento', 'Em_andamento'),   # em andamento
        ('Concluído', 'Concluído'),         # concluido
      
    )

    Título = models.CharField(max_length=255)
    Descrição = models.TextField()
    Arquivo = models.FileField(upload_to='',  blank=True, null=True)
    Status = models.CharField(
        max_length=20,
        choices=STATUS,
    )

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    #com esse comando abaixo pegamos a data da solicitação
    created_at = models.DateTimeField(auto_now_add=True)
    # o comando abaixo serve para sempre que alguém alterar o status o db seja atualizado de acordo
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.Título #com isso no painel terá o título em cada chamado.



