
from unicodedata import name
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "chamado_geral"

urlpatterns = [
    path('', views.chamadosList, name='chamados-list'),
    path('chamado_geral/<int:id>', views.chamadoView, name="chamado-view"),
    path('newChamado/', views.newChamado, name='new-chamado'),
    path('chamadosGerais/', views.chamadosGerais, name='chamadosGerais'),
    path('edit/<int:id>', views.editChamado, name='edit-chamado'),
    path('edit2/<int:id>', views.editChamado2, name='edit-chamado2'),
    path('delete/<int:id>', views.deleteChamado, name='delete-chamado'),
    path('midia/', views.midia, name="midia"),
    path('midia2/', views.midia2, name="midia2"),
    path('admin2/', views.admin2, name='admmin-acess'),
    path('admin3/', views.admin3, name='admmin-acess3'),
]


if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )

