from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.http import HttpResponse
#from urllib import request
from .forms import ChamadoForm, ChamadoForm2
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage #import para visualizar anexos

from .models import Chamado_geral

# Create your views here.
@login_required
def chamadosList(request): #request é a requisição do django
    chamados_list = Chamado_geral.objects.all().order_by('-created_at').filter(user=request.user)  #Pegando todas os chamados do banco para o template.

    paginator = Paginator(chamados_list, 10)
    page = request.GET.get('page')
    chamados = paginator.get_page(page)

    return render(request, 'chamados/list.html', {'chamados': chamados})
   

@login_required
def chamadoView(request, id):
    chamado_geral = get_object_or_404(Chamado_geral, pk=id)
    return render(request, 'chamados/chamado.html', {'chamado': chamado_geral})

@login_required
def newChamado(request):
    if request.method == 'POST':
        form = ChamadoForm(request.POST)

        if form.is_valid():
            chamado_geral = form.save(commit=False) #commit=False serve para que o form só envie dados pro banco após clicar no botão de solicitar.
            chamado_geral.Status = 'Solicitado' #pr-e preenchido com status 'solicitado'
            chamado_geral.user = request.user
            chamado_geral.save()
            messages.info(request, 'Chamado aberto com sucesso!')
            return redirect('/') #/ = nossa primeira página

    else:
        form = ChamadoForm()
        return render(request, 'chamados/addChamado.html', {'form': form})

@login_required
def deleteChamado(request, id):
    chamado = get_object_or_404(Chamado_geral, pk=id)
    chamado.delete()
    messages.info(request, 'Chamado deletado com sucesso!')
    return redirect('/')

@login_required
def editChamado(request, id):
    chamado = get_object_or_404(Chamado_geral, pk=id)
    form = ChamadoForm(instance=chamado)

    if(request.method == 'POST'):
        form = ChamadoForm(request.POST, instance=chamado)

        if(form.is_valid()):
            chamado.save()
            messages.info(request, 'Editado com sucesso!')
            return redirect('/')
        else:
            return render(request, 'chamados/editChamado.html', {'form': form, 'chamado': chamado})
    else:
        return render(request, 'chamados/editChamado.html', {'form': form, 'chamado': chamado})


@login_required
def editChamado2(request, id):
    chamado = get_object_or_404(Chamado_geral, pk=id)
    form = ChamadoForm2(instance=chamado)
    

    if(request.method == 'POST'):
        form = ChamadoForm2(request.POST, instance=chamado)

        if(form.is_valid()):
            #chamado = form.save(commit=False) #commit=False serve para que o form só envie dados pro banco após clicar no botão de solicitar.
            #chamado.user = request.user
            chamado.save()
            messages.info(request, 'Chamado editado com sucesso!')
            return redirect('/admin3/')
        else:
            return render(request, 'chamados/edit2.html', {'form': form, 'chamado': chamado})
    else:
        return render(request, 'chamados/edit2.html', {'form': form, 'chamado': chamado})


@login_required
def chamadosGerais(request):
    chamados = Chamado_geral.objects.all().order_by('-created_at')
    paginator = Paginator(chamados, 10)
    page = request.GET.get('page')
    chamados = paginator.get_page(page)

    return render(request, 'chamados/chamadosGerais.html', {'chamados': chamados})

@login_required
def midia(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'upload.html')


@login_required
def admin2(request):
    if request.method == 'POST':
        form = ChamadoForm2(request.get)

        if form.is_valid():
            chamado_geral = form.save(commit=False) #commit=False serve para que o form só envie dados pro banco após clicar no botão de solicitar.
            #chamado_geral.Status = 'Solicitado' #pr-e preenchido com status 'solicitado'
            chamado_geral.user = request.user
            chamado_geral.save()
            #messages.info(request, 'Chamado aberto com sucesso!')
            return redirect('/') #/ = nossa primeira página

    else:
        form = ChamadoForm2()
        return render(request, 'chamados/admin2.html', {'form': form})



@login_required
def admin3(request):

    chamados = Chamado_geral.objects.all().order_by('-created_at')
    paginator = Paginator(chamados, 10)
    page = request.GET.get('page')
    chamados = paginator.get_page(page)

    return render(request, 'chamados/admin3.html', {'chamados': chamados})



