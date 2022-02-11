from dataclasses import field
from django import forms

from .models import Chamado_geral

class ChamadoForm(forms.ModelForm):
    class Meta:
        model = Chamado_geral
        fields = ('Título', 'Descrição')


class ChamadoForm2(forms.ModelForm):
    class Meta:
        model = Chamado_geral
        fields = ('Título', 'Descrição', 'Arquivo', 'Status')



