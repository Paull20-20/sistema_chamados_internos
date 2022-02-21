from re import search
from django.contrib import admin

from .models import Chamado_geral

class Admin(admin.ModelAdmin):
    list_display = ('user', 'Título', 'Descrição','Arquivo', 'Status') #Campos que irão aparecer na tela de pesquisa do admin
    #list_editable = ('Status',) #Campos editáveis
    reandoly_fields = ('user',) #Campos somente de leitura
    #search_fields = ('user', 'Status',) #Campos que podemos pesquisar na barra de pesquisa
    list_filter = ('user', 'Status',) #Campos nas quais podemos filtrar os dados

admin.site.register(Chamado_geral, Admin)






