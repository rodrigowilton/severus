import os

import requests
import webbrowser
from .models import Unidades
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import StreamingHttpResponse
from .forms import AbastecimentosForm, CondominiosForm, CondominiosEditForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, redirect
from app.models import (Apartamentos, Abastecimentos, AberturasPortas, AcessosApp, AgendamentoHorarios,
Agendamentos, Areas, AreasParalelas, Atendimentos, Atividades, AtividadesMateriaisProdutos, AtividadesOrdemdeservicos,
AuthGroup, AuthGroupPermissions, AuthPermission, AuthUser, AuthUserGroups, AuthUserUserPermissions, CamFacials,
CardsElevadors, CentraisJfls, Chamadas, ChavesVirtuais, ChecklistObras, Codigos, ComercialEtapas, ComercialLeadEtapas,
ComercialLeadProcessos, ComercialLeads, ComercialProcessos, ComercialProspeccao, Comodatos,CondominioEquipamentos,
Condominios, CondominiosFeriados, CondominiosFuncionarios, CondominiosFuncionariosDispositivosRoles, ConfigFacials,
ConfigOs, ContatoEmergencias, ControlesAcessos, Convidados, Criticidades, Departamentos, Dispositivos, DispositivosAcessos,
DispositivosCards, DispositivosCardsTipos, DispositivosEventos, DispositivosMarcas,DispositivosModelos, DispositivosRegistros,
DispositivosRoles, DispositivosRolesDispositivosAcessos, DispositivosTipos, DjangoAdminLog, DjangoContentType,DjangoMigrations,
DjangoSession, Documentos, ElevadorChamados, Empresas, EmpresasServicos, EmpresasServicosEmpresas, Encomendas,
EntregadoresNormas, EstadosEquipamentos, Eventos, EventosTratados,Faturamentos, FaturamentosMateriais,FaturamentosOrcamentos,
Feriados, Ferramentas, Fotos, Funcionarios, GruposEventos, GruposZonas, HistoricoCondominios, HistoricoPessoas, Imagemcameras,
Informativos, Internets, ItensCadastrados, ItensOrcamentos, ItensVistorias, LiberacoesAcessos, LiberacoesChaves, MateriaisAtividades,
MateriaisGrupos, MateriaisMarcas, MateriaisObras, MateriaisProdutos, MateriaisUnidades, MudancasNormas, Notificacoes, Obras,
ObrasChecklistObras, Ocorrencias, Orcamentos, OrcamentosMateriais, OrcamentosPessoas, Ordemdeservicos, OrdemdeservicosMateriaisProdutos,
Parcelas, Patrimonios, Pedagios, PermissaoAcessos, PermissaoAcessosDispositivosRoles, Pessoas, PessoasDispositivosRoles, Pets,
Pgms, PlantaoOcorrencias, PlantaoOperacionals, Portas, PrestadoresAcessos, PrestadoresNormas, Projetos, Qths, QthsTarefas,
QthsTarefasQths, Questionarios, Racas, Recados, ReconhecidoFacials, ReservasNormas, Roles, Sindicos, Subramais, SubtiposOcorrencias,
SubtiposOcorrenciasOcorrencias, SubtiposTiposAbastecimentos, Suporteunidades, Tarefas, TatticaFuncionarios, TatticaTelefones,
TatticaVeiculos, TiposAbastecimentos, TiposAcessos, TiposClassificacaos, TiposCondominiosFuncionarios,TiposControlesAcessos,
TiposElevadorChamados, TiposEncomendas, TiposEquipamentos, TiposEventosTratados, TiposFotos, TiposFuncionarios, TiposOcorrencias,
TiposOcorrenciasOcorrencias, TiposPagamentos, TiposPatrimonios, TiposPedagios, TiposPessoas, TiposProjetos, TiposRacas,
TiposSindicos, TiposTarefas)
from django.http import JsonResponse


def atendimento(request):
    if request.session.get('user'):
        condominios = Condominios.objects.all()  # Pega todos os condomínios do banco

        return render(request, 'atendimento.html', {'condominios': condominios})

    return render(request, 'login.html')


#@login_required(login_url='login')
def index(request):
   if request.session.get('user'):
        condominios = Condominios.objects.all().order_by('nome_condominio')
        return render(request, 'index.html', {'condominios': condominios})

   return render(request, 'login.html')

def condominio(request):
    if request.session.get('user'):
        return render(request, 'condominio.html')

    return render(request, 'login.html')



def unidades(request):
    if request.session.get('user'):
        unidades_list = Unidades.objects.all()
        nomes_unidades = [unidade.nome_unidade for unidade in unidades_list]
        return render(request, 'unidades.html', {'unidades': unidades_list})

    return render(request, 'login.html')

def internets(request):
    if request.session.get('user'):
        internet_list = Internets.objects.all()
        nome_internet = [internet.nome_internet for internet in internet_list]
        return render(request, 'internets.html', {'internets': internet_list})

    return render(request, 'login.html')

def cameras_view(request):
    url = "http://192.168.2.254:8081/#!/login?token=eyJ1c2VyTmFtZSI6ImFkbWluIn0.Wuf-5rC-MmXEaujDUJNCJ_ZZ17GkXC7ljQajDcvOenM&continue={\"path\":\"live\",\"search\":{\"layout\":\"%7B1E813852-98D4-4926-8DD1-1D6F3D15C823%7D\"}}"

    try:
        # Faça a requisição GET
        response = requests.get(url, timeout=10)  # Timeout de 10 segundos

        # Verifique se a requisição foi bem-sucedida
        if response.status_code == 200:
            # Obtenha o conteúdo da resposta
            conteudo = response.text
            # Abrir a resposta no navegador
            webbrowser.open_new(url)
        else:
            conteudo = f"Erro na requisição: {response.status_code}"

    except requests.exceptions.RequestException as e:
        conteudo = f"Ocorreu um erro: {e}"

    #return render(request, 'cameras/cameras.html', {'conteudo': conteudo})
    return render(request, 'index.html', {'conteudo': conteudo})





def agenda(request):
    if request.session.get('user'):
        return render(request, 'menu_agenda.html')

    return render(request, 'login.html')


def config(request):
    if request.session.get('user'):
        return render(request, 'menu_adm.html')

    return render(request, 'login.html')

def contatos(request):
    if request.session.get('user'):
        return render(request, 'menu_contatos.html')

    return render(request, 'login.html')

def informacoes(request):
    if request.session.get('user'):
        return render(request, 'menu_informacoes.html')

    return render(request, 'login.html')

def ocorrencias(request):
    if request.session.get('user'):
        return render(request, 'menu_ocorrencias.html')

    return render(request, 'login.html')

def servicos(request):
    if request.session.get('user'):
        return render(request, 'menu_servicos.html')

    return render(request, 'login.html')

def solicitacoes(request):
    if request.session.get('user'):
        return render(request, 'menu_solicitacoes.html')

    return render(request, 'login.html')

def telefones(request):
    if request.session.get('user'):
        return render(request, 'menu_telefones.html')

    return render(request, 'login.html')

def abastecimento_create(request):
    if request.session.get('user'):
        if request.method == 'POST':
            form = AbastecimentosForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('abastecimentos-list')  # Altere para a rota desejada após o salvamento
        else:
            form = AbastecimentosForm()
        return render(request, 'abastecimentos_form.html', {'form': form})

    return render(request, 'login.html')
def condominio_create(request):
    if request.session.get('user'):
        if request.method == 'POST':
            form = CondominiosForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('condominio_list')  # Ensure this URL name exists in your URL configuration
        else:
            form = CondominiosForm()

        return render(request, 'condominio_form.html', {'form': form})

    return render(request, 'login.html')
def condominio_edit(request, id):
    if request.session.get('user'):
        condominio = get_object_or_404(Condominios, id=id)
        if request.method == "POST":
            form = CondominioForm(request.POST, instance=condominio)
            if form.is_valid():
                form.save()
                # redirecione conforme necessário
        else:
            form = CondominioForm(instance=condominio)
        return render(request, 'condominio_form.html', {'form': form})

    return render(request, 'login.html')

def condominio_list(request):
    if request.session.get('user'):
        condominios = Condominios.objects.all().order_by('nome_condominio')
        return render(request, 'condominios.html', {'condominios': condominios})

    return render(request, 'login.html')

from django.shortcuts import render, get_object_or_404, redirect
from .models import Condominios
from .forms import CondominiosEditForm

def editar_condominio(request, pk):
    if request.session.get('user'):
        condominio = get_object_or_404(Condominios, pk=pk)
        if request.method == 'POST':
            form = CondominiosEditForm(request.POST, instance=condominio)
            if form.is_valid():
                form.save()
                return redirect('index')  # Redireciona para a página inicial após a edição
        else:
            form = CondominiosEditForm(instance=condominio)
        return render(request, 'app/editar_condominio.html', {'form': form, 'condominio': condominio})

    return render(request, 'login.html')


def consultar_condominio(request, pk):
    if request.session.get('user'):
        condominio = get_object_or_404(Condominios, pk=pk)
        return render(request, 'app/consultar_condominio.html', {'condominio': condominio})

    return render(request, 'login.html')