
from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.chamadosList, name='chamados-list'),
    path('chamado_geral/<int:id>', views.chamadoView, name="chamado-view"),
    path('newChamado/', views.newChamado, name='new-chamado'),
    path('chamadosGerais/', views.chamadosGerais, name='chamadosGerais'),
    path('edit/<int:id>', views.editChamado, name='edit-chamado'),
    path('edit2/<int:id>', views.editChamado2, name='edit-chamado2'),
    path('delete/<int:id>', views.deleteChamado, name='delete-chamado'),
    path('midia/', views.midia, name="midia"),
    path('admin2/', views.admin2, name='admmin-acess'),
    path('admin3/', views.admin3, name='admmin-acess3'),
]






