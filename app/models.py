# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Abastecimentos(models.Model):
    tattica_veiculo = models.ForeignKey('TatticaVeiculos', models.DO_NOTHING)
    tattica_funcionario = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING, blank=True, null=True)
    tipos_abastecimento = models.ForeignKey('TiposAbastecimentos', models.DO_NOTHING)
    data_abastecimento = models.DateField()
    km_atual = models.CharField(max_length=45, blank=True, null=True)
    numero_bloco = models.CharField(max_length=45, blank=True, null=True)
    qtd_litros = models.CharField(max_length=45, blank=True, null=True)
    total = models.CharField(max_length=45, blank=True, null=True)
    valor_por_litro = models.CharField(max_length=45, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'abastecimentos'


class AberturasPortas(models.Model):
    pgm = models.ForeignKey('Pgms', models.DO_NOTHING)
    tattica_funcionario = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING, blank=True, null=True)
    pessoa = models.ForeignKey('Pessoas', models.DO_NOTHING, blank=True, null=True)
    condominios_funcionario = models.ForeignKey('CondominiosFuncionarios', models.DO_NOTHING, blank=True, null=True)
    liberacoes_chave = models.ForeignKey('LiberacoesChaves', models.DO_NOTHING, blank=True, null=True)
    lat = models.CharField(max_length=45, blank=True, null=True)
    lng = models.CharField(max_length=45, blank=True, null=True)
    distancia = models.IntegerField(blank=True, null=True)
    qrcode = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=45, blank=True, null=True)
    user_agent = models.CharField(max_length=225, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aberturas_portas'


class AcessosApp(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    data_acesso = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acessos_app'


class AgendamentoHorarios(models.Model):
    condominio = models.ForeignKey('Condominios', models.DO_NOTHING)
    area = models.ForeignKey('Areas', models.DO_NOTHING)
    horario_inicio = models.CharField(max_length=20)
    horario_fim = models.CharField(max_length=20)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agendamento_horarios'


class Agendamentos(models.Model):
    condominio = models.ForeignKey('Condominios', models.DO_NOTHING)
    area = models.ForeignKey('Areas', models.DO_NOTHING)
    apartamento = models.ForeignKey('Apartamentos', models.DO_NOTHING, blank=True, null=True)
    tattica_funcionario = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING, blank=True, null=True)
    pessoa = models.ForeignKey('Pessoas', models.DO_NOTHING, blank=True, null=True)
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    hora_inicio = models.CharField(max_length=20, blank=True, null=True)
    hora_fim = models.CharField(max_length=20, blank=True, null=True)
    mudanca = models.IntegerField(blank=True, null=True)
    outrostext = models.TextField(blank=True, null=True)
    adm = models.IntegerField(db_comment='1 - Informar; 2 - Ciente ')
    zelador = models.IntegerField(db_comment='1 - Informar; 2 - Ciente')
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agendamentos'


class Apartamentos(models.Model):
    condominio = models.ForeignKey('Condominios', models.DO_NOTHING)
    nome_apartamento = models.CharField(max_length=45)
    ramal_apartamento = models.CharField(max_length=45, blank=True, null=True)
    telefone = models.CharField(max_length=45, blank=True, null=True)
    senha = models.CharField(max_length=10, blank=True, null=True)
    observacao = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apartamentos'


class Areas(models.Model):
    condominio = models.ForeignKey('Condominios', models.DO_NOTHING)
    nome_area = models.CharField(max_length=220, db_collation='latin1_swedish_ci')
    andar = models.CharField(max_length=45, db_collation='latin1_swedish_ci', blank=True, null=True)
    limite_pessoas = models.IntegerField(blank=True, null=True)
    valor = models.CharField(max_length=45, db_collation='latin1_swedish_ci', blank=True, null=True)
    normas = models.TextField(db_collation='latin1_swedish_ci', blank=True, null=True)
    info = models.TextField(db_collation='latin1_swedish_ci', blank=True, null=True)
    cor = models.CharField(max_length=20, db_collation='latin1_swedish_ci', blank=True, null=True)
    pgm = models.ForeignKey('Pgms', models.DO_NOTHING, blank=True, null=True)
    hora_min = models.CharField(max_length=6, db_collation='latin1_swedish_ci', blank=True, null=True)
    hora_max = models.CharField(max_length=6, db_collation='latin1_swedish_ci', blank=True, null=True)
    antecedencia_min = models.CharField(max_length=9, db_collation='latin1_swedish_ci', blank=True, null=True)
    antecedencia_max = models.IntegerField(blank=True, null=True)
    intervalo_entre_reservas = models.CharField(max_length=6, db_collation='latin1_swedish_ci', blank=True, null=True)
    max_abertos = models.IntegerField(blank=True, null=True)
    tempo_entre_reservas = models.IntegerField(blank=True, null=True)
    tipo_reserva = models.IntegerField(blank=True, null=True)
    hora_inicio_permitido = models.CharField(max_length=6, db_collation='latin1_swedish_ci', blank=True, null=True)
    hora_fim_permitido = models.CharField(max_length=6, db_collation='latin1_swedish_ci', blank=True, null=True)
    hora_inicio_permitido_fds = models.CharField(max_length=6, blank=True, null=True)
    hora_fim_permitido_fds = models.CharField(max_length=6, blank=True, null=True)
    segunda = models.IntegerField(blank=True, null=True)
    terca = models.IntegerField(blank=True, null=True)
    quarta = models.IntegerField(blank=True, null=True)
    quinta = models.IntegerField(blank=True, null=True)
    sexta = models.IntegerField(blank=True, null=True)
    sabado = models.IntegerField(blank=True, null=True)
    domingo = models.IntegerField(blank=True, null=True)
    tem_feriados = models.IntegerField(blank=True, null=True)
    permite_convidados = models.IntegerField(blank=True, null=True)
    necessita_aprovacao = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'areas'


class AreasParalelas(models.Model):
    area = models.ForeignKey(Areas, models.DO_NOTHING)
    area2 = models.ForeignKey(Areas, models.DO_NOTHING, related_name='areasparalelas_area2_set')
    tipo = models.IntegerField(db_comment='1 - Concorrente / 2 - Conjunto')
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'areas_paralelas'


class Atendimentos(models.Model):
    condominio = models.ForeignKey('Condominios', models.DO_NOTHING)
    chamada = models.ForeignKey('Chamadas', models.DO_NOTHING, blank=True, null=True)
    tattica_funcionario = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING)
    liberacoes_acesso = models.ForeignKey('LiberacoesAcessos', models.DO_NOTHING, blank=True, null=True)
    apartamento = models.ForeignKey(Apartamentos, models.DO_NOTHING, blank=True, null=True)
    condominios_funcionario = models.ForeignKey('CondominiosFuncionarios', models.DO_NOTHING, blank=True, null=True)
    pessoa = models.ForeignKey('Pessoas', models.DO_NOTHING, blank=True, null=True)
    funcionario = models.ForeignKey('Funcionarios', models.DO_NOTHING, blank=True, null=True)
    empresa = models.ForeignKey('Empresas', models.DO_NOTHING, blank=True, null=True)
    tipo_atendimento = models.IntegerField(blank=True, null=True)
    busca = models.CharField(max_length=100, blank=True, null=True)
    acoes = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'atendimentos'


class Atividades(models.Model):
    ocorrencia = models.ForeignKey('Ocorrencias', models.DO_NOTHING, blank=True, null=True)
    departamento = models.ForeignKey('Departamentos', models.DO_NOTHING)
    tattica_funcionario = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING, blank=True, null=True)
    colaborador = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING, related_name='atividades_colaborador_set', blank=True, null=True)
    atividade = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    descricao = models.TextField()
    observacao = models.TextField(blank=True, null=True)
    local = models.IntegerField(db_comment='1 - Interno; 2 - Externo')
    pin_status = models.IntegerField(blank=True, null=True, db_comment='1 - pinned; 0 - unpinned;')
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    observacao_cli = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'atividades'


class AtividadesMateriaisProdutos(models.Model):
    atividade = models.ForeignKey(Atividades, models.DO_NOTHING)
    materiais_produto = models.ForeignKey('MateriaisProdutos', models.DO_NOTHING)
    qtd = models.CharField(max_length=45)
    data_saida = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'atividades_materiais_produtos'


class AtividadesOrdemdeservicos(models.Model):
    atividade = models.ForeignKey(Atividades, models.DO_NOTHING)
    ordemdeservico = models.ForeignKey('Ordemdeservicos', models.DO_NOTHING)
    resolucao = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'atividades_ordemdeservicos'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CamFacials(models.Model):
    config_facial = models.ForeignKey('ConfigFacials', models.DO_NOTHING)
    condominio = models.ForeignKey('Condominios', models.DO_NOTHING)
    active = models.IntegerField()
    name = models.CharField(max_length=45)
    url = models.CharField(max_length=255)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    gamma = models.IntegerField(blank=True, null=True)
    tolerance = models.IntegerField(blank=True, null=True)
    threshold = models.IntegerField(blank=True, null=True)
    roi_left = models.IntegerField(blank=True, null=True)
    roi_top = models.IntegerField(blank=True, null=True)
    roi_right = models.IntegerField(blank=True, null=True)
    roi_bottom = models.IntegerField(blank=True, null=True)
    pgm = models.ForeignKey('Pgms', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cam_facials'


class CardsElevadors(models.Model):
    dispositivo = models.ForeignKey('Dispositivos', models.DO_NOTHING)
    nome_cartao = models.CharField(max_length=45)
    codigo = models.CharField(max_length=45)
    ativado = models.IntegerField()
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cards_elevadors'


class CentraisJfls(models.Model):
    condominio = models.ForeignKey('Condominios', models.DO_NOTHING)
    ip = models.CharField(max_length=45)
    modelo = models.CharField(max_length=45, blank=True, null=True)
    versao = models.CharField(max_length=8, blank=True, null=True)
    mac = models.CharField(max_length=45, blank=True, null=True)
    ativada = models.IntegerField()
    data_ultima_conexao = models.DateTimeField(blank=True, null=True)
    part1 = models.IntegerField()
    part2 = models.IntegerField()
    part3 = models.IntegerField()
    part4 = models.IntegerField()
    sirene = models.IntegerField()
    problema = models.IntegerField()
    ordem = models.IntegerField()
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'centrais_jfls'


class Chamadas(models.Model):
    condominio = models.ForeignKey('Condominios', models.DO_NOTHING)
    tattica_funcionario = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING, blank=True, null=True)
    tip = models.ForeignKey('Tips', models.DO_NOTHING, blank=True, null=True)
    audio = models.CharField(max_length=45, blank=True, null=True)
    digitado_para = models.CharField(max_length=45, blank=True, null=True)
    duracao = models.CharField(max_length=45, blank=True, null=True)
    tempo_espera = models.CharField(max_length=45, blank=True, null=True)
    data_start = models.DateTimeField()
    data_atendimento = models.DateTimeField(blank=True, null=True)
    data_desligamento = models.DateTimeField()
    ptah_js = models.IntegerField()
    atendeu = models.IntegerField()
    status = models.IntegerField(db_comment='1 - Atendendo, 2 - Ligando')
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chamadas'


class ChavesVirtuais(models.Model):
    liberacoes_acesso = models.ForeignKey('LiberacoesAcessos', models.DO_NOTHING, blank=True, null=True)
    link_chave = models.CharField(unique=True, max_length=100)
    qtd_max = models.IntegerField(blank=True, null=True)
    qtd_usado = models.IntegerField(blank=True, null=True)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    hora_inicio = models.CharField(max_length=50, blank=True, null=True)
    hora_fim = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chaves_virtuais'


class ChecklistObras(models.Model):
    nome = models.CharField(max_length=220)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'checklist_obras'


class Codigos(models.Model):
    condominio = models.ForeignKey('Condominios', models.DO_NOTHING)
    apartamento = models.ForeignKey(Apartamentos, models.DO_NOTHING)
    pessoa = models.ForeignKey('Pessoas', models.DO_NOTHING, blank=True, null=True)
    codigo = models.CharField(unique=True, max_length=45)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'codigos'


class ComercialEtapas(models.Model):
    nome = models.CharField(max_length=50)
    tempo = models.IntegerField(blank=True, null=True)
    ordem = models.IntegerField()
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comercial_etapas'


class ComercialLeadEtapas(models.Model):
    comercial_lead = models.ForeignKey('ComercialLeads', models.DO_NOTHING)
    comercial_etapa = models.ForeignKey(ComercialEtapas, models.DO_NOTHING)
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    obs = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comercial_lead_etapas'


class ComercialLeadProcessos(models.Model):
    comercial_lead = models.ForeignKey('ComercialLeads', models.DO_NOTHING)
    comercial_processo = models.ForeignKey('ComercialProcessos', models.DO_NOTHING)
    colaborador = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING)
    data_execucao = models.DateField()
    situacao = models.IntegerField()
    obs = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comercial_lead_processos'


class ComercialLeads(models.Model):
    nome = models.CharField(max_length=225, blank=True, null=True)
    endereco = models.CharField(max_length=225, blank=True, null=True)
    responsavel = models.CharField(max_length=225, blank=True, null=True)
    cargo = models.CharField(max_length=45, blank=True, null=True)
    telefone = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    forma_contato = models.CharField(max_length=45, blank=True, null=True)
    tipo_portaria = models.IntegerField(blank=True, null=True)
    problema_relatado = models.CharField(max_length=255, blank=True, null=True)
    qtde_apartamentos = models.IntegerField(blank=True, null=True)
    forma_encontrou_tattica = models.CharField(max_length=225, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comercial_leads'


class ComercialProcessos(models.Model):
    nome = models.CharField(max_length=225)
    descricao = models.CharField(max_length=255)
    tempo = models.IntegerField(blank=True, null=True)
    comercial_etapa = models.ForeignKey(ComercialEtapas, models.DO_NOTHING)
    colaborador = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING, blank=True, null=True)
    obrigatorio = models.IntegerField(blank=True, null=True)
    arquivo_processo = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comercial_processos'


class ComercialProspeccao(models.Model):
    cond_nome = models.CharField(max_length=100, blank=True, null=True, db_comment='Nome do condomÝnio a qual o contato estß realizando o contato.')
    contato_nome = models.CharField(max_length=100, blank=True, null=True, db_comment='Nome do contato que fez a prospecþÒo')
    contato_telefone = models.CharField(max_length=45, blank=True, null=True, db_comment='Telefone do contato que fez a prospecþÒo.')
    contato_email = models.CharField(max_length=100, blank=True, null=True, db_comment='Email do contato a qual estß realizando a prospecþÒo.')
    contato_cargo = models.CharField(max_length=45, blank=True, null=True, db_comment='Cargo do contato no condomÝnio a qual estß realizando a prospecþÒo. ')
    contato_origem = models.CharField(max_length=45, blank=True, null=True, db_comment='Como contato ficou sabendo a respeito da Tattica.')
    cond_qtd_apt = models.IntegerField(blank=True, null=True, db_comment='Quantidade de apartamento dentro do condomÝnio a qual estß realizando a prospecþÒo.')
    cond_tipo_port = models.CharField(max_length=45, blank=True, null=True, db_comment='Tipo de portaria no condomÝnio a qual estß realizando a prospecþÒo.')
    observacao = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comercial_prospeccao'


class Comodatos(models.Model):
    tattica_funcionario = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING)
    patrimonio = models.ForeignKey('Patrimonios', models.DO_NOTHING)
    data_inicio = models.DateField(blank=True, null=True)
    data_fim = models.DateField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comodatos'


class CondominioEquipamentos(models.Model):
    condominio = models.ForeignKey('Condominios', models.DO_NOTHING)
    tipos_equipamentos = models.ForeignKey('TiposEquipamentos', models.DO_NOTHING)
    estado_equipamento = models.ForeignKey('EstadosEquipamentos', models.DO_NOTHING)
    nome_condequipamento = models.CharField(max_length=220)
    modelo = models.CharField(max_length=220, blank=True, null=True)
    marca = models.CharField(max_length=220, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    data_instalacao = models.DateField(blank=True, null=True)
    valor_condequipamento = models.FloatField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'condominio_equipamentos'


class Condominios(models.Model):
    internet = models.ForeignKey('Internets', models.DO_NOTHING)
    unidade = models.ForeignKey('Unidades', models.DO_NOTHING)
    suporteunidade = models.ForeignKey('Suporteunidades', models.DO_NOTHING)
    entregadores_norma = models.ForeignKey('EntregadoresNormas', models.DO_NOTHING)
    prestadores_norma = models.ForeignKey('PrestadoresNormas', models.DO_NOTHING)
    reservas_norma = models.ForeignKey('ReservasNormas', models.DO_NOTHING)
    mudancas_norma = models.ForeignKey('MudancasNormas', models.DO_NOTHING)
    responsavel_tattica = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING, blank=True, null=True)
    norma_observacao = models.TextField(blank=True, null=True)
    nome_condominio = models.CharField(max_length=220)
    data_condominio = models.DateField(blank=True, null=True)
    dias_implantacao = models.IntegerField(blank=True, null=True)
    ramal_condominio = models.CharField(max_length=45, blank=True, null=True)
    ramal_interno = models.CharField(max_length=45, blank=True, null=True)
    cnpj = models.CharField(max_length=45, blank=True, null=True)
    logradouro = models.CharField(max_length=220, blank=True, null=True)
    numero = models.CharField(max_length=20, blank=True, null=True)
    complemento = models.CharField(max_length=220, blank=True, null=True)
    bairro = models.CharField(max_length=220, blank=True, null=True)
    cidade = models.CharField(max_length=220, blank=True, null=True)
    uf = models.CharField(max_length=5, blank=True, null=True)
    cep = models.CharField(max_length=45, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    cameras_usuario = models.CharField(max_length=45, blank=True, null=True)
    cameras_senha = models.CharField(max_length=45, blank=True, null=True)
    cameras_usuario_sindico = models.CharField(max_length=45, blank=True, null=True)
    cameras_senha_sindico = models.CharField(max_length=45, blank=True, null=True)
    website = models.CharField(max_length=220, blank=True, null=True)
    website_agendamento = models.CharField(max_length=225, blank=True, null=True)
    telefone = models.CharField(max_length=45, blank=True, null=True)
    financeiro_responsavel = models.CharField(max_length=220, blank=True, null=True)
    financeiro_email = models.CharField(max_length=220, blank=True, null=True)
    arquivo_contrato = models.CharField(max_length=200, blank=True, null=True)
    acesso_aplicativo = models.IntegerField(blank=True, null=True)
    mod_acessos = models.IntegerField(blank=True, null=True)
    mod_qrcode = models.IntegerField(blank=True, null=True)
    mod_chave_virtual = models.IntegerField(blank=True, null=True)
    dias_chave_virtual = models.IntegerField(blank=True, null=True)
    distancia = models.IntegerField(blank=True, null=True)
    link_ri = models.CharField(max_length=220, blank=True, null=True)
    empresa = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'condominios'


class CondominiosFeriados(models.Model):
    condominio = models.ForeignKey(Condominios, models.DO_NOTHING)
    feriado = models.ForeignKey('Feriados', models.DO_NOTHING)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'condominios_feriados'


class CondominiosFuncionarios(models.Model):
    tipos_condominios_funcionario = models.ForeignKey('TiposCondominiosFuncionarios', models.DO_NOTHING)
    condominio = models.ForeignKey(Condominios, models.DO_NOTHING)
    nome_condominios_funcionario = models.CharField(max_length=220)
    telefone1 = models.CharField(max_length=45, blank=True, null=True)
    telefone2 = models.CharField(max_length=45, blank=True, null=True)
    hora_inicio = models.CharField(max_length=20, blank=True, null=True)
    hora_inicio_sab = models.CharField(max_length=20, blank=True, null=True)
    hora_fim_sab = models.CharField(max_length=20, blank=True, null=True)
    hora_fim = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'condominios_funcionarios'


class CondominiosFuncionariosDispositivosRoles(models.Model):
    condominios_funcionario = models.ForeignKey(CondominiosFuncionarios, models.DO_NOTHING)
    dispositivos_role = models.ForeignKey('DispositivosRoles', models.DO_NOTHING)
    status = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'condominios_funcionarios_dispositivos_roles'


class ConfigFacials(models.Model):
    nome_sv = models.CharField(max_length=45)
    ip_sv = models.CharField(max_length=45)
    gui = models.IntegerField()
    extract = models.IntegerField()
    resize = models.IntegerField()
    win_size = models.IntegerField()
    show_match = models.IntegerField()
    step_frame = models.IntegerField()
    tolerance = models.IntegerField()
    threshold = models.IntegerField()
    resolution_x = models.IntegerField()
    resolution_y = models.IntegerField()
    webhook = models.CharField(max_length=255)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'config_facials'


class ConfigOs(models.Model):
    hora_inicio = models.CharField(max_length=6)
    hora_fim = models.CharField(max_length=6)
    motivo = models.CharField(max_length=225, blank=True, null=True)
    ativo = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'config_os'


class ContatoEmergencias(models.Model):
    apartamento = models.ForeignKey(Apartamentos, models.DO_NOTHING)
    nome = models.CharField(max_length=220)
    celular = models.CharField(max_length=45)
    celular_2 = models.CharField(max_length=45, blank=True, null=True)
    parentesco = models.CharField(max_length=200, blank=True, null=True)
    obs = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contato_emergencias'


class ControlesAcessos(models.Model):
    condominio = models.ForeignKey(Condominios, models.DO_NOTHING)
    tipos_controles_acesso = models.ForeignKey('TiposControlesAcessos', models.DO_NOTHING)
    tattica_funcionario = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING, blank=True, null=True)
    apartamento = models.ForeignKey(Apartamentos, models.DO_NOTHING, blank=True, null=True)
    pessoa = models.ForeignKey('Pessoas', models.DO_NOTHING, blank=True, null=True)
    condominios_funcionario = models.ForeignKey(CondominiosFuncionarios, models.DO_NOTHING, blank=True, null=True)
    sindico = models.ForeignKey('Sindicos', models.DO_NOTHING, blank=True, null=True)
    entregador = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING, related_name='controlesacessos_entregador_set', blank=True, null=True)
    realizador = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING, related_name='controlesacessos_realizador_set', blank=True, null=True)
    solicitante = models.CharField(max_length=100, blank=True, null=True)
    execucao = models.IntegerField(blank=True, null=True, db_comment='1 - Presencial; 2 - Remoto')
    pedido = models.IntegerField(blank=True, null=True, db_comment='1 - Gratuito, 2 - Aguardando Pagamento, 6  - A receber em dinheiro, 7 - A receber por Pagseguro, 8 - A receber por transferÛncia, 3 - Pago em dinheiro, 5 - Pago por Pagseguro, 4 - Pago por transferÛncia, 9 - Em Analise')
    quantidade = models.IntegerField(blank=True, null=True)
    valor = models.CharField(max_length=45, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    identificador = models.TextField(blank=True, null=True)
    agendado = models.IntegerField(blank=True, null=True, db_comment='0 - Pedido normal; 1 - Pedido agendado; ')
    promo_status = models.IntegerField(blank=True, null=True)
    data_prazo = models.DateField(blank=True, null=True)
    data_entrega = models.DateTimeField(blank=True, null=True)
    data_final = models.DateField(blank=True, null=True)
    data_pagamento = models.DateTimeField(blank=True, null=True)
    comprador_nome = models.CharField(max_length=255, blank=True, null=True)
    comprador_email = models.CharField(max_length=255, blank=True, null=True)
    comprador_cpf = models.CharField(max_length=15, blank=True, null=True)
    comprador_telefone = models.CharField(max_length=15, blank=True, null=True)
    metodo_pagamento = models.IntegerField(blank=True, null=True, db_comment='1 - CartÒo de CrÚdito, 2 - Boleto, 3 - DÚbito, 4 - Saldo PagSeguro, 5 - Oi Paggo, 7 - DÚposito em conta, 11 - PIX')
    link_boleto = models.TextField(blank=True, null=True)
    codigo_pagseguro = models.CharField(max_length=255, blank=True, null=True)
    status_pagseguro = models.IntegerField(blank=True, null=True, db_comment='1 - Aguardando Pagamento, 2 - Em analise, 3 - Paga, 4 - DisponÝvel, 5 - Em disputa, 6 - Devolvida, 7 - Cancelada, 8 - Debitado, 9 - RetenþÒo temporßria')
    status = models.IntegerField(db_comment='0 - Deletado\n1 - Pendente\n2 - a Entregar\n3 - Resolvido')
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'controles_acessos'


class Convidados(models.Model):
    agendamento = models.ForeignKey(Agendamentos, models.DO_NOTHING)
    nome_convidado = models.CharField(max_length=220)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'convidados'


class Criticidades(models.Model):
    nome_criticidade = models.CharField(max_length=100)
    icone_criticidade = models.CharField(max_length=45)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'criticidades'


class Departamentos(models.Model):
    nome_departamento = models.CharField(max_length=45)
    sigla = models.CharField(max_length=45, blank=True, null=True)
    ramal_departamento = models.CharField(max_length=45, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departamentos'


class Dispositivos(models.Model):
    condominio = models.ForeignKey(Condominios, models.DO_NOTHING)
    dispositivos_modelo = models.ForeignKey('DispositivosModelos', models.DO_NOTHING)
    nome_dispositivo = models.CharField(max_length=45)
    ip = models.CharField(max_length=45)
    versao = models.CharField(max_length=45, blank=True, null=True)
    mac = models.CharField(max_length=45, blank=True, null=True)
    device_id = models.BigIntegerField(blank=True, null=True)
    device_name = models.CharField(max_length=45, blank=True, null=True)
    data_ultima_conexao = models.DateTimeField(blank=True, null=True)
    user = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dispositivos'


class DispositivosAcessos(models.Model):
    dispositivo = models.ForeignKey(Dispositivos, models.DO_NOTHING)
    nome_acesso = models.CharField(max_length=45)
    codigo = models.CharField(max_length=45)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dispositivos_acessos'


class DispositivosCards(models.Model):
    condominios_funcionario = models.ForeignKey(CondominiosFuncionarios, models.DO_NOTHING, blank=True, null=True)
    tattica_funcionario = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING, blank=True, null=True)
    apartamento = models.ForeignKey(Apartamentos, models.DO_NOTHING, blank=True, null=True)
    pessoa = models.ForeignKey('Pessoas', models.DO_NOTHING, blank=True, null=True)
    permissao_acessos = models.ForeignKey('PermissaoAcessos', models.DO_NOTHING, blank=True, null=True)
    dispositivos_cards_tipo = models.ForeignKey('DispositivosCardsTipos', models.DO_NOTHING)
    veiculo = models.ForeignKey('Veiculos', models.DO_NOTHING, blank=True, null=True)
    nome_card = models.CharField(max_length=45, blank=True, null=True)
    codigo = models.CharField(max_length=45, blank=True, null=True)
    biometria = models.TextField(blank=True, null=True)
    face = models.TextField(blank=True, null=True)
    timestamp = models.IntegerField(blank=True, null=True)
    finger_position = models.IntegerField(blank=True, null=True)
    data_bloqueio = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dispositivos_cards'


class DispositivosCardsTipos(models.Model):
    nome_card_tipo = models.CharField(max_length=45)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dispositivos_cards_tipos'


class DispositivosEventos(models.Model):
    evento = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dispositivos_eventos'


class DispositivosMarcas(models.Model):
    nome_marca = models.CharField(max_length=45)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dispositivos_marcas'


class DispositivosModelos(models.Model):
    dispositivos_tipo = models.ForeignKey('DispositivosTipos', models.DO_NOTHING)
    dispositivos_marca = models.ForeignKey(DispositivosMarcas, models.DO_NOTHING)
    nome_modelo = models.CharField(max_length=45)
    identificador = models.CharField(max_length=45)
    biometria = models.IntegerField()
    tag = models.IntegerField()
    rf433 = models.IntegerField()
    senha = models.IntegerField()
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dispositivos_modelos'


class DispositivosRegistros(models.Model):
    dispositivos_card = models.ForeignKey(DispositivosCards, models.DO_NOTHING, blank=True, null=True)
    dispositivos_acesso = models.ForeignKey(DispositivosAcessos, models.DO_NOTHING, blank=True, null=True)
    dispositivo = models.ForeignKey(Dispositivos, models.DO_NOTHING, blank=True, null=True)
    pessoa = models.ForeignKey('Pessoas', models.DO_NOTHING, blank=True, null=True)
    condominios_funcionario = models.ForeignKey(CondominiosFuncionarios, models.DO_NOTHING, blank=True, null=True)
    tattica_funcionario = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING, blank=True, null=True)
    permissao_acessos = models.ForeignKey('PermissaoAcessos', models.DO_NOTHING, blank=True, null=True)
    card_elevador = models.ForeignKey(CardsElevadors, models.DO_NOTHING, blank=True, null=True)
    dispositivos_evento = models.ForeignKey(DispositivosEventos, models.DO_NOTHING, blank=True, null=True)
    codigo_card = models.CharField(max_length=45, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dispositivos_registros'


class DispositivosRoles(models.Model):
    condominio = models.ForeignKey(Condominios, models.DO_NOTHING)
    nome_role = models.CharField(max_length=45)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dispositivos_roles'


class DispositivosRolesDispositivosAcessos(models.Model):
    dispositivos_role = models.ForeignKey(DispositivosRoles, models.DO_NOTHING)
    dispositivos_acesso = models.ForeignKey(DispositivosAcessos, models.DO_NOTHING)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dispositivos_roles_dispositivos_acessos'


class DispositivosTipos(models.Model):
    nome_tipo = models.CharField(max_length=45)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dispositivos_tipos'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Documentos(models.Model):
    condominio = models.ForeignKey(Condominios, models.DO_NOTHING)
    apartamento = models.ForeignKey(Apartamentos, models.DO_NOTHING, blank=True, null=True)
    nome_documento = models.CharField(max_length=45)
    arquivo = models.CharField(max_length=220)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documentos'


class ElevadorChamados(models.Model):
    condominio = models.ForeignKey(Condominios, models.DO_NOTHING)
    tattica_funcionario = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING)
    empresa = models.ForeignKey('Empresas', models.DO_NOTHING)
    tipos_elevador_chamado = models.ForeignKey('TiposElevadorChamados', models.DO_NOTHING)
    sindico = models.ForeignKey('Sindicos', models.DO_NOTHING, blank=True, null=True)
    condominios_funcionario = models.ForeignKey(CondominiosFuncionarios, models.DO_NOTHING, blank=True, null=True)
    apartamento = models.ForeignKey(Apartamentos, models.DO_NOTHING, blank=True, null=True)
    pessoa = models.ForeignKey('Pessoas', models.DO_NOTHING, blank=True, null=True)
    tattica_solicitante = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING, related_name='elevadorchamados_tattica_solicitante_set', blank=True, null=True)
    solicitante = models.CharField(max_length=200, blank=True, null=True)
    elevador = models.CharField(max_length=150)
    protocolo = models.CharField(max_length=45)
    atendente = models.CharField(max_length=150)
    andar = models.CharField(max_length=45, blank=True, null=True)
    hora_ligacao = models.CharField(max_length=45)
    descricao = models.TextField()
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elevador_chamados'


class Empresas(models.Model):
    razao_social = models.CharField(max_length=220, blank=True, null=True)
    nome_fantasia = models.CharField(max_length=220)
    cnpj = models.CharField(max_length=45, blank=True, null=True)
    imagem = models.CharField(max_length=45, blank=True, null=True)
    website = models.CharField(max_length=220, blank=True, null=True)
    telefone = models.CharField(max_length=45, blank=True, null=True)
    celular = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=220, blank=True, null=True)
    logradouro = models.CharField(max_length=220, blank=True, null=True)
    numero = models.CharField(max_length=20, blank=True, null=True)
    complemento = models.CharField(max_length=220, blank=True, null=True)
    bairro = models.CharField(max_length=220, blank=True, null=True)
    cidade = models.CharField(max_length=220, blank=True, null=True)
    uf = models.CharField(max_length=5, blank=True, null=True)
    cep = models.CharField(max_length=45, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresas'


class EmpresasServicos(models.Model):
    nome_tipos_empresa = models.CharField(max_length=220)
    cor = models.CharField(max_length=20, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresas_servicos'


class EmpresasServicosEmpresas(models.Model):
    empresas_servico = models.ForeignKey(EmpresasServicos, models.DO_NOTHING)
    empresa = models.ForeignKey(Empresas, models.DO_NOTHING)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresas_servicos_empresas'


class Encomendas(models.Model):
    condominio = models.ForeignKey(Condominios, models.DO_NOTHING)
    apartamento = models.ForeignKey(Apartamentos, models.DO_NOTHING, blank=True, null=True)
    tattica_funcionario = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING)
    tipos_encomenda = models.ForeignKey('TiposEncomendas', models.DO_NOTHING)
    transportadora = models.CharField(max_length=100, blank=True, null=True)
    entregador = models.CharField(max_length=100, blank=True, null=True)
    remetente = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    data_recebimento = models.DateField()
    hora_recebimento = models.CharField(max_length=20)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'encomendas'


class EntregadoresNormas(models.Model):
    nome_entregador_normas = models.CharField(max_length=220)
    cor = models.CharField(max_length=20, blank=True, null=True)
    icone = models.CharField(max_length=45, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entregadores_normas'


class EstadosEquipamentos(models.Model):
    nome_estados_equipamento = models.CharField(max_length=220)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estados_equipamentos'


class Eventos(models.Model):
    centrais_jfl = models.ForeignKey(CentraisJfls, models.DO_NOTHING)
    tipos_evento = models.ForeignKey('TiposEventos', models.DO_NOTHING)
    zona = models.ForeignKey('Zonas', models.DO_NOTHING, blank=True, null=True)
    pgm = models.ForeignKey('Pgms', models.DO_NOTHING, blank=True, null=True)
    conta = models.CharField(max_length=4, blank=True, null=True)
    contador = models.CharField(max_length=4, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eventos'


class EventosTratados(models.Model):
    tipos_eventos_tratado = models.ForeignKey('TiposEventosTratados', models.DO_NOTHING)
    tattica_funcionario = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING)
    evento = models.ForeignKey(Eventos, models.DO_NOTHING, blank=True, null=True)
    descricao = models.TextField()
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eventos_tratados'


class Faturamentos(models.Model):
    tattica_funcionario = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING, blank=True, null=True)
    condominio = models.ForeignKey(Condominios, models.DO_NOTHING)
    tipos_pagamento = models.ForeignKey('TiposPagamentos', models.DO_NOTHING)
    parcelas = models.ForeignKey('Parcelas', models.DO_NOTHING, blank=True, null=True)
    nome_faturamento = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    desconto = models.TextField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faturamentos'


class FaturamentosMateriais(models.Model):
    faturamento = models.ForeignKey(Faturamentos, models.DO_NOTHING)
    materiais_produtos = models.ForeignKey('MateriaisProdutos', models.DO_NOTHING)
    produtos_qtd = models.IntegerField(blank=True, null=True)
    valor = models.CharField(max_length=45, blank=True, null=True)
    desconto = models.CharField(max_length=45, blank=True, null=True)
    valor_custo = models.CharField(max_length=45, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faturamentos_materiais'


class FaturamentosOrcamentos(models.Model):
    faturamento = models.ForeignKey(Faturamentos, models.DO_NOTHING)
    orcamento = models.ForeignKey('Orcamentos', models.DO_NOTHING)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faturamentos_orcamentos'


class Feriados(models.Model):
    nome = models.CharField(max_length=45)
    data = models.CharField(max_length=5)
    sinc_acessos = models.IntegerField()
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feriados'


class Ferramentas(models.Model):
    tattica_funcionario = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING, blank=True, null=True)
    tattica_supervisor = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING, related_name='ferramentas_tattica_supervisor_set', blank=True, null=True)
    fornecedor = models.CharField(max_length=45, blank=True, null=True)
    nome_ferramenta = models.CharField(max_length=45, blank=True, null=True)
    qtde = models.IntegerField(blank=True, null=True)
    valor = models.CharField(max_length=45, blank=True, null=True)
    num_nota = models.CharField(max_length=45, blank=True, null=True)
    data_compra = models.DateField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ferramentas'


class Fotos(models.Model):
    condominio = models.ForeignKey(Condominios, models.DO_NOTHING)
    tipos_foto = models.ForeignKey('TiposFotos', models.DO_NOTHING)
    nome_foto = models.CharField(max_length=220, blank=True, null=True)
    imagem_foto = models.CharField(max_length=220)
    foto_dir = models.CharField(max_length=220)
    type = models.CharField(max_length=220)
    descricao = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fotos'


class Funcionarios(models.Model):
    empresa = models.ForeignKey(Empresas, models.DO_NOTHING, blank=True, null=True)
    tipos_funcionario = models.ForeignKey('TiposFuncionarios', models.DO_NOTHING, blank=True, null=True)
    nome_funcionario = models.CharField(max_length=220)
    cargo = models.CharField(max_length=220, blank=True, null=True)
    cpf = models.CharField(max_length=45, blank=True, null=True)
    rg = models.CharField(max_length=45, blank=True, null=True)
    telefone = models.CharField(max_length=45, blank=True, null=True)
    celular = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=220, blank=True, null=True)
    imagem_prestador = models.CharField(max_length=220, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'funcionarios'


class GruposEventos(models.Model):
    nome_grupo_evento = models.CharField(max_length=45)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grupos_eventos'


class GruposZonas(models.Model):
    nome_grupo_zona = models.CharField(max_length=45)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grupos_zonas'


class HistoricoCondominios(models.Model):
    condominio = models.ForeignKey(Condominios, models.DO_NOTHING)
    tattica_funcionario = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING)
    pessoa = models.ForeignKey('Pessoas', models.DO_NOTHING, blank=True, null=True)
    condominios_funcionario = models.ForeignKey(CondominiosFuncionarios, models.DO_NOTHING, blank=True, null=True)
    sindico = models.ForeignKey('Sindicos', models.DO_NOTHING, blank=True, null=True)
    tipo_contato = models.IntegerField()
    data_execucao = models.DateField(blank=True, null=True)
    hora_execucao = models.CharField(max_length=45, blank=True, null=True)
    assunto = models.CharField(max_length=255, blank=True, null=True)
    obs = models.TextField(blank=True, null=True)
    alertar = models.IntegerField(blank=True, null=True)
    arquivo = models.CharField(max_length=225, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historico_condominios'


class HistoricoPessoas(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    pessoa = models.ForeignKey('Pessoas', models.DO_NOTHING)
    apartamento_id = models.IntegerField(blank=True, null=True)
    tipos_pessoa_id = models.IntegerField(blank=True, null=True)
    criticidade_id = models.IntegerField(blank=True, null=True)
    responsavel = models.IntegerField(blank=True, null=True)
    nome_pessoa = models.CharField(max_length=220, blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    cpf = models.CharField(max_length=45, blank=True, null=True)
    rg = models.CharField(max_length=45, blank=True, null=True)
    data_aniversario = models.DateField(blank=True, null=True)
    parentesco = models.CharField(max_length=220, blank=True, null=True)
    observacao = models.CharField(max_length=220, blank=True, null=True)
    celular = models.CharField(max_length=45, blank=True, null=True)
    celular_2 = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=220, blank=True, null=True)
    profissao = models.CharField(max_length=45, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historico_pessoas'


class Imagemcameras(models.Model):
    condominio = models.ForeignKey(Condominios, models.DO_NOTHING)
    tattica_funcionario_id = models.IntegerField(blank=True, null=True)
    tattica_solicitante = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING, blank=True, null=True)
    apartamento_id = models.IntegerField(blank=True, null=True)
    pessoa_id = models.IntegerField(blank=True, null=True)
    sindico_id = models.IntegerField(blank=True, null=True)
    condominios_funcionario = models.ForeignKey(CondominiosFuncionarios, models.DO_NOTHING, blank=True, null=True)
    solicitante = models.CharField(max_length=220, blank=True, null=True)
    cameras = models.CharField(max_length=220)
    periodo = models.TextField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    link = models.CharField(max_length=250, blank=True, null=True)
    tipo_gravacao = models.IntegerField(db_comment='1 - Imagem, 2 - Audio')
    execucao = models.IntegerField(db_comment='1 - Presencial; 2 - Remoto')
    aprovacao = models.IntegerField()
    area_sindico = models.IntegerField(db_comment='0-nÒo; 1-sim')
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imagemcameras'


class Informativos(models.Model):
    titulo = models.CharField(max_length=220)
    mensagem = models.TextField()
    imagem = models.CharField(max_length=255, blank=True, null=True)
    condominio = models.ForeignKey(Condominios, models.DO_NOTHING, blank=True, null=True)
    apartamento = models.ForeignKey(Apartamentos, models.DO_NOTHING, blank=True, null=True)
    pessoa = models.ForeignKey('Pessoas', models.DO_NOTHING, blank=True, null=True)
    log_quem_recebeu = models.TextField(blank=True, null=True)
    status_notification = models.IntegerField(blank=True, null=True)
    total_enviado = models.IntegerField(blank=True, null=True)
    total_recebido = models.IntegerField(blank=True, null=True)
    usuario = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'informativos'


class Internets(models.Model):
    nome_internet = models.CharField(max_length=220)
    empresa = models.CharField(max_length=220)
    telefone = models.CharField(max_length=45, blank=True, null=True)
    telefone2 = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=220, blank=True, null=True)
    website = models.CharField(max_length=220, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'internets'


class ItensCadastrados(models.Model):
    nome_item = models.CharField(max_length=220)
    valor_unitario = models.FloatField()
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itens_cadastrados'


class ItensOrcamentos(models.Model):
    orcamento = models.ForeignKey('Orcamentos', models.DO_NOTHING)
    itens_cadastrado = models.ForeignKey(ItensCadastrados, models.DO_NOTHING)
    qtd_item = models.IntegerField()
    valor_unitario = models.FloatField()
    valor_total = models.FloatField()
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itens_orcamentos'


class ItensVistorias(models.Model):
    nome_itens_vistoria = models.CharField(max_length=220)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itens_vistorias'


class LiberacoesAcessos(models.Model):
    condominio = models.ForeignKey(Condominios, models.DO_NOTHING)
    apartamento = models.ForeignKey(Apartamentos, models.DO_NOTHING, blank=True, null=True)
    pessoa = models.ForeignKey('Pessoas', models.DO_NOTHING, blank=True, null=True)
    tattica_funcionario = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING, blank=True, null=True)
    nome_acesso = models.CharField(max_length=220, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    rg = models.CharField(max_length=45, blank=True, null=True)
    cpf = models.CharField(max_length=45, blank=True, null=True)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'liberacoes_acessos'


class LiberacoesChaves(models.Model):
    liberacoes_acesso = models.ForeignKey(LiberacoesAcessos, models.DO_NOTHING)
    chave = models.CharField(max_length=45)
    qtd_max = models.IntegerField()
    qtd_usado = models.IntegerField()
    data_inicio = models.DateField()
    data_fim = models.DateField()
    hora_inicio = models.CharField(max_length=45)
    hora_fim = models.CharField(max_length=45)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'liberacoes_chaves'


class MateriaisAtividades(models.Model):
    atividade = models.ForeignKey(Atividades, models.DO_NOTHING)
    nome_material = models.CharField(max_length=220)
    qtd = models.CharField(max_length=45)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'materiais_atividades'


class MateriaisGrupos(models.Model):
    nome_grupo = models.CharField(max_length=100)
    status = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'materiais_grupos'


class MateriaisMarcas(models.Model):
    nome_marca = models.CharField(max_length=100)
    observacao_marca = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'materiais_marcas'


class MateriaisObras(models.Model):
    obra = models.ForeignKey('Obras', models.DO_NOTHING)
    nome_material = models.CharField(max_length=220)
    qtd = models.CharField(max_length=45)
    data_material = models.DateField()
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'materiais_obras'


class MateriaisProdutos(models.Model):
    materiais_grupo = models.ForeignKey(MateriaisGrupos, models.DO_NOTHING)
    materiais_marca = models.ForeignKey(MateriaisMarcas, models.DO_NOTHING)
    materiais_unidade = models.ForeignKey('MateriaisUnidades', models.DO_NOTHING)
    materiais_tipo = models.IntegerField(blank=True, null=True)
    nome_produto = models.CharField(max_length=100)
    observacao_produto = models.TextField(blank=True, null=True)
    codigo = models.CharField(max_length=45, blank=True, null=True)
    custo = models.CharField(max_length=45)
    valor = models.CharField(max_length=45)
    listar_app = models.IntegerField(blank=True, null=True)
    implantacao = models.IntegerField(blank=True, null=True)
    max_desc = models.IntegerField(blank=True, null=True, db_comment='Maximo de desconto para este produto.')
    status = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'materiais_produtos'


class MateriaisUnidades(models.Model):
    nome_unidade = models.CharField(max_length=100)
    status = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'materiais_unidades'


class MudancasNormas(models.Model):
    nome_mudanca_normas = models.CharField(max_length=220)
    cor = models.CharField(max_length=20)
    icone = models.CharField(max_length=45)
    status = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mudancas_normas'


class Notificacoes(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    responsavel = models.ForeignKey('Users', models.DO_NOTHING, related_name='notificacoes_responsavel_set', blank=True, null=True)
    tipo = models.IntegerField()
    titulo = models.CharField(max_length=220)
    mensagem = models.TextField()
    status = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'notificacoes'


class Obras(models.Model):
    condominio = models.ForeignKey(Condominios, models.DO_NOTHING)
    data_inicio = models.DateField(blank=True, null=True)
    data_final = models.DateField(blank=True, null=True)
    data_previsao = models.DateField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'obras'


class ObrasChecklistObras(models.Model):
    obra = models.ForeignKey(Obras, models.DO_NOTHING)
    checklist_obra = models.ForeignKey(ChecklistObras, models.DO_NOTHING)
    data_inicio = models.DateField(blank=True, null=True)
    data_fim = models.DateField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'obras_checklist_obras'


class Ocorrencias(models.Model):
    condominio = models.ForeignKey(Condominios, models.DO_NOTHING)
    tattica_funcionario = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING, blank=True, null=True)
    apartamento = models.ForeignKey(Apartamentos, models.DO_NOTHING, blank=True, null=True)
    pessoa = models.ForeignKey('Pessoas', models.DO_NOTHING, blank=True, null=True)
    condominios_funcionario = models.ForeignKey(CondominiosFuncionarios, models.DO_NOTHING, blank=True, null=True)
    tattica_solicitante = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING, related_name='ocorrencias_tattica_solicitante_set', blank=True, null=True)
    sindico = models.ForeignKey('Sindicos', models.DO_NOTHING, blank=True, null=True)
    departamento = models.ForeignKey(Departamentos, models.DO_NOTHING)
    ocorrencia = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    solicitante = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField()
    observacao = models.TextField(blank=True, null=True)
    atividades_count = models.IntegerField()
    atividades_pendentes_count = models.IntegerField()
    criticidade = models.IntegerField(blank=True, null=True, db_comment='0 - Normal; 1 - CrÝtico;')
    relevancia = models.IntegerField(blank=True, null=True)
    area_sindico = models.IntegerField(db_comment='0-nÒo; 1-sim')
    status = models.IntegerField(db_comment='0 - Deletado; 1 - Pendente; 2 - Resolvido; 3 - Duplicado')
    email_send = models.IntegerField(blank=True, null=True, db_comment='1 - NÒo enviado; 2 - Enviado')
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ocorrencias'


class Orcamentos(models.Model):
    tattica_funcionario = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING, blank=True, null=True)
    orcamento_nome = models.CharField(max_length=100, blank=True, null=True, db_comment='"ID" do orþamento')
    orcamento_tipo = models.IntegerField(blank=True, null=True)
    condominio = models.ForeignKey(Condominios, models.DO_NOTHING, blank=True, null=True)
    comercial_lead = models.ForeignKey(ComercialLeads, models.DO_NOTHING, blank=True, null=True)
    ocorrencia = models.ForeignKey(Ocorrencias, models.DO_NOTHING, blank=True, null=True)
    empresa = models.CharField(max_length=45, blank=True, null=True)
    assunto = models.CharField(max_length=225, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)
    pdfurl = models.CharField(max_length=100, blank=True, null=True)
    desconto = models.IntegerField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    data_diagnostico = models.DateField(blank=True, null=True)
    status = models.IntegerField(db_comment='0 - CriaþÒo; 1 - Pendente; 2 - Aprovado; 3 - Cancelado; 4 - Concluido')
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orcamentos'


class OrcamentosMateriais(models.Model):
    orcamento = models.ForeignKey(Orcamentos, models.DO_NOTHING)
    materiais_produtos = models.ForeignKey(MateriaisProdutos, models.DO_NOTHING)
    produtos_qtd = models.IntegerField(blank=True, null=True)
    valor = models.CharField(max_length=45, blank=True, null=True, db_comment='Valor em que foi vendido a unidade')
    desconto = models.CharField(max_length=45, blank=True, null=True)
    valor_custo = models.CharField(max_length=45, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orcamentos_materiais'


class OrcamentosPessoas(models.Model):
    orcamento = models.ForeignKey(Orcamentos, models.DO_NOTHING)
    pessoa = models.ForeignKey('Pessoas', models.DO_NOTHING)
    status = models.IntegerField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orcamentos_pessoas'


class Ordemdeservicos(models.Model):
    condominio = models.ForeignKey(Condominios, models.DO_NOTHING)
    tattica_funcionario = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING)
    tattica_ajudante = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING, related_name='ordemdeservicos_tattica_ajudante_set', blank=True, null=True)
    hora_entrada = models.TimeField(blank=True, null=True)
    hora_saida = models.TimeField(blank=True, null=True)
    data_os = models.DateField(blank=True, null=True)
    possui_faturamento = models.IntegerField(blank=True, null=True)
    obs = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ordemdeservicos'


class OrdemdeservicosMateriaisProdutos(models.Model):
    ordemdeservico = models.ForeignKey(Ordemdeservicos, models.DO_NOTHING)
    materiais_produto = models.ForeignKey(MateriaisProdutos, models.DO_NOTHING)
    qtde = models.IntegerField()
    status = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ordemdeservicos_materiais_produtos'


class Parcelas(models.Model):
    parcela = models.IntegerField()
    min_valor = models.TextField(db_comment='Valor minimo para aplicar parcela.')
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parcelas'


class Patrimonios(models.Model):
    tipos_patrimonio = models.ForeignKey('TiposPatrimonios', models.DO_NOTHING)
    departamento = models.ForeignKey(Departamentos, models.DO_NOTHING)
    estados_equipamento = models.ForeignKey(EstadosEquipamentos, models.DO_NOTHING)
    tattica_funcionario = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING, blank=True, null=True)
    nome_patrimonio = models.CharField(max_length=220)
    modelo = models.CharField(max_length=220, blank=True, null=True)
    local = models.CharField(max_length=220, blank=True, null=True)
    data_compra = models.DateField(blank=True, null=True)
    valor_patrimonio = models.FloatField(blank=True, null=True)
    durabilidade = models.IntegerField(blank=True, null=True)
    depreciacao = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patrimonios'


class Pedagios(models.Model):
    tipos_pedagio = models.ForeignKey('TiposPedagios', models.DO_NOTHING)
    tattica_funcionario = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING)
    tipos_veiculo = models.ForeignKey('TiposVeiculos', models.DO_NOTHING)
    data_pedagio = models.DateField()
    qtd = models.IntegerField()
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedagios'


class PermissaoAcessos(models.Model):
    tipos_acesso = models.ForeignKey('TiposAcessos', models.DO_NOTHING)
    condominio = models.ForeignKey(Condominios, models.DO_NOTHING)
    apartamento = models.ForeignKey(Apartamentos, models.DO_NOTHING, blank=True, null=True)
    empresas_servicos_empresa = models.ForeignKey(EmpresasServicosEmpresas, models.DO_NOTHING, blank=True, null=True)
    funcionario = models.ForeignKey(Funcionarios, models.DO_NOTHING, blank=True, null=True)
    data_inicio = models.DateField(blank=True, null=True)
    data_fim = models.DateField(blank=True, null=True)
    domingo = models.IntegerField()
    segunda = models.IntegerField()
    terca = models.IntegerField()
    quarta = models.IntegerField()
    quinta = models.IntegerField()
    sexta = models.IntegerField()
    sabado = models.IntegerField()
    acesso_livre = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissao_acessos'


class PermissaoAcessosDispositivosRoles(models.Model):
    permissao_acesso = models.ForeignKey(PermissaoAcessos, models.DO_NOTHING)
    dispositivos_role = models.ForeignKey(DispositivosRoles, models.DO_NOTHING)
    status = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissao_acessos_dispositivos_roles'


class Pessoas(models.Model):
    apartamento = models.ForeignKey(Apartamentos, models.DO_NOTHING)
    tipos_pessoa = models.ForeignKey('TiposPessoas', models.DO_NOTHING)
    criticidade = models.ForeignKey(Criticidades, models.DO_NOTHING, blank=True, null=True)
    tipos_classificacao = models.ForeignKey('TiposClassificacaos', models.DO_NOTHING, blank=True, null=True)
    responsavel = models.IntegerField(db_comment='1 - Sim, 2 - NÒo')
    nome_pessoa = models.CharField(max_length=220, blank=True, null=True)
    imagem_pessoa = models.CharField(max_length=255, blank=True, null=True)
    sexo = models.CharField(max_length=1)
    cpf = models.CharField(max_length=45, blank=True, null=True)
    rg = models.CharField(max_length=45, blank=True, null=True)
    data_aniversario = models.DateField(blank=True, null=True)
    parentesco = models.CharField(max_length=220, blank=True, null=True)
    observacao = models.CharField(max_length=220, blank=True, null=True)
    celular = models.CharField(max_length=45, blank=True, null=True)
    celular_2 = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=220, blank=True, null=True)
    profissao = models.CharField(max_length=45, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pessoas'


class PessoasDispositivosRoles(models.Model):
    pessoa = models.ForeignKey(Pessoas, models.DO_NOTHING)
    dispositivos_role = models.ForeignKey(DispositivosRoles, models.DO_NOTHING)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pessoas_dispositivos_roles'


class Pets(models.Model):
    apartamento = models.ForeignKey(Apartamentos, models.DO_NOTHING)
    raca = models.ForeignKey('Racas', models.DO_NOTHING)
    nome_pet = models.CharField(max_length=100)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pets'


class Pgms(models.Model):
    centrais_jfl = models.ForeignKey(CentraisJfls, models.DO_NOTHING)
    nome_pgm = models.CharField(max_length=45)
    nome_exibicao = models.CharField(max_length=60, blank=True, null=True)
    codigo = models.IntegerField()
    visivel_morador = models.IntegerField()
    visivel_visitante = models.IntegerField()
    visivel_sindico = models.IntegerField(blank=True, null=True)
    retencao = models.IntegerField()
    bloqueio = models.IntegerField(blank=True, null=True)
    reserva = models.IntegerField(blank=True, null=True)
    codigo_camera = models.CharField(max_length=45, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pgms'


class PlantaoOcorrencias(models.Model):
    plantao_operacional = models.ForeignKey('PlantaoOperacionals', models.DO_NOTHING)
    ocorrencia = models.TextField()
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plantao_ocorrencias'


class PlantaoOperacionals(models.Model):
    supervisor1 = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING)
    supervisor2 = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING, related_name='plantaooperacionals_supervisor2_set', blank=True, null=True)
    unidade = models.ForeignKey('Unidades', models.DO_NOTHING, blank=True, null=True)
    data_abertura = models.DateField()
    data_fechamento = models.DateField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plantao_operacionals'


class Portas(models.Model):
    porta_nome = models.CharField(max_length=55)
    cond = models.ForeignKey(Condominios, models.DO_NOTHING)
    senha_dispositivo = models.ForeignKey(DispositivosModelos, models.DO_NOTHING, blank=True, null=True)
    tag_dispositivo = models.ForeignKey(DispositivosModelos, models.DO_NOTHING, related_name='portas_tag_dispositivo_set', blank=True, null=True)
    bio_dispositivo = models.ForeignKey(DispositivosModelos, models.DO_NOTHING, related_name='portas_bio_dispositivo_set', blank=True, null=True)
    ctrlgar_dispositivo = models.ForeignKey(DispositivosModelos, models.DO_NOTHING, related_name='portas_ctrlgar_dispositivo_set', blank=True, null=True)
    a1 = models.CharField(max_length=45, blank=True, null=True)
    a2 = models.CharField(max_length=45, blank=True, null=True)
    created = models.DateField(blank=True, null=True)
    modified = models.DateField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portas'


class PrestadoresAcessos(models.Model):
    condominio = models.ForeignKey(Condominios, models.DO_NOTHING)
    empresas_servicos_empresa = models.ForeignKey(EmpresasServicosEmpresas, models.DO_NOTHING)
    funcionario = models.ForeignKey(Funcionarios, models.DO_NOTHING, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prestadores_acessos'


class PrestadoresNormas(models.Model):
    nome_prestador_normas = models.CharField(max_length=220)
    cor = models.CharField(max_length=20, blank=True, null=True)
    icone = models.CharField(max_length=45, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prestadores_normas'


class Projetos(models.Model):
    tipos_projeto = models.ForeignKey('TiposProjetos', models.DO_NOTHING)
    departamento = models.ForeignKey(Departamentos, models.DO_NOTHING)
    tattica_funcionario = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING)
    nome_projeto = models.CharField(max_length=45)
    descricao = models.TextField()
    data_inicio = models.DateField(blank=True, null=True)
    data_fim = models.DateField(blank=True, null=True)
    data_previsao = models.DateField(blank=True, null=True)
    tarefas_count = models.IntegerField()
    tarefas_pendentes_count = models.IntegerField()
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projetos'


class Qths(models.Model):
    tattica_funcionario = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING)
    condominio = models.ForeignKey(Condominios, models.DO_NOTHING)
    data_visita = models.DateTimeField(blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qths'


class QthsTarefas(models.Model):
    nome_tarefa = models.CharField(max_length=100)
    ordem = models.IntegerField()
    icon = models.CharField(max_length=45)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qths_tarefas'


class QthsTarefasQths(models.Model):
    qth = models.ForeignKey(Qths, models.DO_NOTHING)
    qths_tarefa = models.ForeignKey(QthsTarefas, models.DO_NOTHING)
    resposta_tarefa = models.IntegerField(db_comment='0 - sem, 1 - ok e 2 - nÒo')
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qths_tarefas_qths'


class Questionarios(models.Model):
    condominio = models.ForeignKey(Condominios, models.DO_NOTHING)
    pessoa = models.ForeignKey(Pessoas, models.DO_NOTHING, blank=True, null=True)
    nome_pessoa = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    pergunta1 = models.IntegerField(blank=True, null=True)
    pergunta2 = models.IntegerField(blank=True, null=True)
    pergunta3 = models.IntegerField(blank=True, null=True)
    pergunta4 = models.IntegerField(blank=True, null=True)
    pergunta5 = models.IntegerField(blank=True, null=True)
    pergunta6 = models.IntegerField(blank=True, null=True)
    pergunta7 = models.IntegerField(blank=True, null=True)
    sugestao = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questionarios'


class Racas(models.Model):
    tipos_raca = models.ForeignKey('TiposRacas', models.DO_NOTHING)
    nome_raca = models.CharField(max_length=100)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'racas'


class Recados(models.Model):
    condominio = models.ForeignKey(Condominios, models.DO_NOTHING)
    apartamento = models.ForeignKey(Apartamentos, models.DO_NOTHING, blank=True, null=True)
    pessoa = models.ForeignKey(Pessoas, models.DO_NOTHING, blank=True, null=True)
    tattica_funcionario = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING, blank=True, null=True)
    nome_recado = models.CharField(max_length=220, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    data_inicio = models.DateField()
    data_fim = models.DateField()

    class Meta:
        managed = False
        db_table = 'recados'


class ReconhecidoFacials(models.Model):
    pessoa = models.ForeignKey(Pessoas, models.DO_NOTHING)
    condominio = models.ForeignKey(Condominios, models.DO_NOTHING)
    cam_facial = models.ForeignKey(CamFacials, models.DO_NOTHING)
    foto_face = models.CharField(max_length=255)
    data_reconhecimento = models.DateTimeField()
    dataset_pasta = models.CharField(max_length=255)
    abriu_porta = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reconhecido_facials'


class ReservasNormas(models.Model):
    nome_reserva_normas = models.CharField(max_length=220)
    cor = models.CharField(max_length=20, blank=True, null=True)
    icone = models.CharField(max_length=45, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reservas_normas'


class Roles(models.Model):
    nome_role = models.CharField(max_length=220)
    identificador = models.CharField(max_length=220)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Sindicos(models.Model):
    condominio = models.ForeignKey(Condominios, models.DO_NOTHING)
    pessoa = models.ForeignKey(Pessoas, models.DO_NOTHING)
    tipos_sindico = models.ForeignKey('TiposSindicos', models.DO_NOTHING)
    email_sindico = models.CharField(max_length=200, blank=True, null=True)
    data_inicio = models.DateField(blank=True, null=True)
    data_fim = models.DateField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    email_permissao = models.IntegerField()
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sindicos'


class Subramais(models.Model):
    condominio = models.ForeignKey(Condominios, models.DO_NOTHING)
    numero = models.CharField(max_length=45)
    local = models.CharField(max_length=45, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subramais'


class SubtiposOcorrencias(models.Model):
    nome_subtipos_ocorrencia = models.CharField(max_length=220)
    tipos_ocorrencia = models.ForeignKey('TiposOcorrencias', models.DO_NOTHING)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subtipos_ocorrencias'


class SubtiposOcorrenciasOcorrencias(models.Model):
    ocorrencia = models.ForeignKey(Ocorrencias, models.DO_NOTHING)
    subtipos_ocorrencia = models.ForeignKey(SubtiposOcorrencias, models.DO_NOTHING)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subtipos_ocorrencias_ocorrencias'


class SubtiposTiposAbastecimentos(models.Model):
    nome_subtipo = models.CharField(max_length=100)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subtipos_tipos_abastecimentos'


class Suporteunidades(models.Model):
    nome_suporteunidade = models.CharField(max_length=100)
    status = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'suporteunidades'


class Tarefas(models.Model):
    tipos_tarefa = models.ForeignKey('TiposTarefas', models.DO_NOTHING, blank=True, null=True)
    tattica_funcionario = models.ForeignKey('TatticaFuncionarios', models.DO_NOTHING)
    projeto = models.ForeignKey(Projetos, models.DO_NOTHING)
    descricao = models.TextField()
    observacao = models.TextField(blank=True, null=True)
    resolucao = models.TextField(blank=True, null=True)
    data_inicio = models.DateField(blank=True, null=True)
    data_fim = models.DateField(blank=True, null=True)
    data_previsao = models.DateField(blank=True, null=True)
    link = models.CharField(max_length=250, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tarefas'


class TatticaFuncionarios(models.Model):
    departamento = models.ForeignKey(Departamentos, models.DO_NOTHING)
    imagem_funcionario = models.CharField(max_length=45, blank=True, null=True)
    nome_funcionario = models.CharField(max_length=220)
    apelido = models.CharField(max_length=200, blank=True, null=True)
    cargo = models.CharField(max_length=45, blank=True, null=True)
    rg = models.CharField(max_length=45, blank=True, null=True)
    cpf = models.CharField(max_length=45, blank=True, null=True)
    carteira_trabalho = models.CharField(max_length=45, blank=True, null=True)
    logradouro = models.CharField(max_length=220, blank=True, null=True)
    numero = models.CharField(max_length=45, blank=True, null=True)
    complemento = models.CharField(max_length=220, blank=True, null=True)
    bairro = models.CharField(max_length=220, blank=True, null=True)
    cidade = models.CharField(max_length=220, blank=True, null=True)
    uf = models.CharField(max_length=10, blank=True, null=True)
    cep = models.CharField(max_length=45, blank=True, null=True)
    telefone = models.CharField(max_length=45, blank=True, null=True)
    celular = models.CharField(max_length=45, blank=True, null=True)
    hora_inicio = models.CharField(max_length=20, blank=True, null=True)
    hora_fim = models.CharField(max_length=20, blank=True, null=True)
    data_adimissao = models.DateField(blank=True, null=True)
    data_demissao = models.DateField(blank=True, null=True)
    telefone_contato = models.CharField(max_length=45, blank=True, null=True)
    plano_saude = models.CharField(max_length=220, blank=True, null=True)
    tipo_sangue = models.CharField(max_length=45, blank=True, null=True)
    escala = models.CharField(max_length=220, blank=True, null=True)
    cnh = models.CharField(max_length=45, blank=True, null=True)
    cnh_data = models.DateField(blank=True, null=True)
    cnh_tipo = models.CharField(max_length=45, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tattica_funcionarios'


class TatticaTelefones(models.Model):
    condominio = models.ForeignKey(Condominios, models.DO_NOTHING, blank=True, null=True)
    departamento = models.ForeignKey(Departamentos, models.DO_NOTHING, blank=True, null=True)
    telefone = models.CharField(max_length=45)
    marca = models.CharField(max_length=45, blank=True, null=True)
    serie = models.CharField(max_length=45, blank=True, null=True)
    imei1 = models.CharField(max_length=45, blank=True, null=True)
    imei2 = models.CharField(max_length=45, blank=True, null=True)
    acessorios = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tattica_telefones'


class TatticaVeiculos(models.Model):
    tipos_veiculo = models.ForeignKey('TiposVeiculos', models.DO_NOTHING)
    marca = models.CharField(max_length=45)
    modelo = models.CharField(max_length=45)
    placa = models.CharField(max_length=45)
    chassi = models.CharField(max_length=45, blank=True, null=True)
    data_compra = models.DateField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    cor = models.CharField(max_length=45)
    ano = models.CharField(max_length=45)
    proprietario = models.IntegerField(db_comment='1 - veiculo da tattica\n2 - externo')
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tattica_veiculos'


class TiposAbastecimentos(models.Model):
    nome_abastecimentos = models.CharField(max_length=220)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    subtipos_tipos_abastecimentos = models.ForeignKey(SubtiposTiposAbastecimentos, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_abastecimentos'


class TiposAcessos(models.Model):
    nome_tipos_acesso = models.CharField(max_length=220, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_acessos'


class TiposClassificacaos(models.Model):
    nome_classificacao = models.CharField(max_length=45)
    texto_classificacao = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_classificacaos'


class TiposCondominiosFuncionarios(models.Model):
    nome_tipo_funcionario = models.CharField(max_length=45)
    status = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_condominios_funcionarios'


class TiposControlesAcessos(models.Model):
    nome_tipos_controles_acesso = models.CharField(max_length=220)
    visivel_morador = models.IntegerField(blank=True, null=True)
    valor = models.CharField(max_length=45, blank=True, null=True)
    link_pagamento = models.CharField(max_length=255, blank=True, null=True)
    valor_promo = models.CharField(max_length=45, blank=True, null=True)
    link_promo = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_controles_acessos'


class TiposElevadorChamados(models.Model):
    nome_tipo_chamado = models.CharField(max_length=150)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_elevador_chamados'


class TiposEncomendas(models.Model):
    nome_tipos_encomenda = models.CharField(max_length=220)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_encomendas'


class TiposEquipamentos(models.Model):
    nome_tipos_condequipamento = models.CharField(max_length=220)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_equipamentos'


class TiposEventos(models.Model):
    grupos_evento = models.ForeignKey(GruposEventos, models.DO_NOTHING)
    nome_tipo_evento = models.CharField(max_length=75)
    codigo_tipo_evento = models.CharField(max_length=4)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_eventos'


class TiposEventosTratados(models.Model):
    nome_tipo_evento_tratado = models.CharField(max_length=100)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_eventos_tratados'


class TiposFotos(models.Model):
    nome_tipos_foto = models.CharField(max_length=220)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_fotos'


class TiposFuncionarios(models.Model):
    nome_tipos_funcionario = models.CharField(max_length=220)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_funcionarios'


class TiposOcorrencias(models.Model):
    nome_tipos_ocorrencia = models.CharField(max_length=220)
    departamento_id = models.IntegerField(blank=True, null=True)
    visivel_app = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_ocorrencias'


class TiposOcorrenciasOcorrencias(models.Model):
    ocorrencia = models.ForeignKey(Ocorrencias, models.DO_NOTHING)
    tipos_ocorrencia = models.ForeignKey(TiposOcorrencias, models.DO_NOTHING)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_ocorrencias_ocorrencias'


class TiposPagamentos(models.Model):
    nome_tipos_pagamento = models.CharField(max_length=220)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_pagamentos'


class TiposPatrimonios(models.Model):
    nome_tipos_patrimonio = models.CharField(max_length=220)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_patrimonios'


class TiposPedagios(models.Model):
    nome_tipos_pedagio = models.CharField(max_length=45)
    valor = models.CharField(max_length=45)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_pedagios'


class TiposPessoas(models.Model):
    nome_tipos_pessoa = models.CharField(max_length=220)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_pessoas'


class TiposProjetos(models.Model):
    nome_tipo_projeto = models.CharField(max_length=45)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_projetos'


class TiposRacas(models.Model):
    nome_tipos_raca = models.CharField(max_length=100)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_racas'


class TiposSindicos(models.Model):
    nome_tipos_sindico = models.CharField(max_length=100)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_sindicos'


class TiposTarefas(models.Model):
    tipos_projeto = models.ForeignKey(TiposProjetos, models.DO_NOTHING)
    tipo_tarefa_nome = models.CharField(max_length=45)
    etapa = models.IntegerField()
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_tarefas'


class TiposVeiculos(models.Model):
    nome_tipos_veiculo = models.CharField(max_length=220)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_veiculos'


class TiposZonas(models.Model):
    codigo_tipo_zona = models.CharField(max_length=2)
    nome_tipo_zona = models.CharField(max_length=45)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_zonas'


class Tips(models.Model):
    unidade = models.ForeignKey('Unidades', models.DO_NOTHING)
    nome_tip = models.CharField(max_length=100)
    ptah_user = models.CharField(max_length=50)
    ip_tip = models.CharField(max_length=50)
    ramal_ptah = models.CharField(max_length=45)
    endpoint = models.CharField(max_length=45)
    mac = models.CharField(max_length=45)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tips'


class TipsTatticaFuncionarios(models.Model):
    tip = models.ForeignKey(Tips, models.DO_NOTHING)
    tattica_funcionario = models.ForeignKey(TatticaFuncionarios, models.DO_NOTHING)
    data_logout = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tips_tattica_funcionarios'


class Unidades(models.Model):
    nome_unidade = models.CharField(max_length=100)
    status = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unidades'


class Users(models.Model):
    role = models.ForeignKey(Roles, models.DO_NOTHING)
    unidade = models.ForeignKey(Unidades, models.DO_NOTHING, blank=True, null=True)
    suporteunidade = models.ForeignKey(Suporteunidades, models.DO_NOTHING, blank=True, null=True)
    pessoa = models.ForeignKey(Pessoas, models.DO_NOTHING, blank=True, null=True)
    tattica_funcionario_id = models.IntegerField(blank=True, null=True)
    condominios_funcionario = models.ForeignKey(CondominiosFuncionarios, models.DO_NOTHING, blank=True, null=True)
    username = models.CharField(max_length=45)
    email = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=255)
    codigo = models.CharField(max_length=45, blank=True, null=True)
    notificacao_ronda = models.IntegerField(blank=True, null=True)
    token_gos = models.CharField(max_length=255, blank=True, null=True)
    acessos = models.IntegerField(blank=True, null=True)
    data_acesso = models.DateTimeField(blank=True, null=True)
    check_lgpd = models.IntegerField(blank=True, null=True)
    permissao_os = models.IntegerField()
    permissao_pgm = models.IntegerField()
    permissao_qth = models.IntegerField()
    permissao_historico = models.IntegerField()
    permissao_ca = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Vagas(models.Model):
    apartamento = models.ForeignKey(Apartamentos, models.DO_NOTHING)
    numero = models.CharField(max_length=45)
    andar = models.CharField(max_length=45)
    descricao = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vagas'


class Veiculos(models.Model):
    apartamento = models.ForeignKey(Apartamentos, models.DO_NOTHING)
    tipos_veiculo = models.ForeignKey(TiposVeiculos, models.DO_NOTHING)
    marca = models.CharField(max_length=220)
    modelo = models.CharField(max_length=220, blank=True, null=True)
    cor = models.CharField(max_length=45, blank=True, null=True)
    placa = models.CharField(max_length=45, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'veiculos'


class Vistorias(models.Model):
    condominio = models.ForeignKey(Condominios, models.DO_NOTHING)
    tattica_funcionario = models.ForeignKey(TatticaFuncionarios, models.DO_NOTHING)
    relato = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vistorias'


class VistoriasItensVistorias(models.Model):
    vistoria = models.ForeignKey(Vistorias, models.DO_NOTHING)
    itens_vistoria = models.ForeignKey(ItensVistorias, models.DO_NOTHING)
    ordem = models.IntegerField()
    descricao = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vistorias_itens_vistorias'


class Zonas(models.Model):
    centrais_jfl = models.ForeignKey(CentraisJfls, models.DO_NOTHING)
    tipos_zona = models.ForeignKey(TiposZonas, models.DO_NOTHING)
    grupos_zona = models.ForeignKey(GruposZonas, models.DO_NOTHING)
    nome_zona = models.CharField(max_length=45)
    codigo_zona = models.CharField(max_length=2)
    particao_a = models.IntegerField()
    particao_b = models.IntegerField()
    particao_c = models.IntegerField()
    particao_d = models.IntegerField()
    stay = models.IntegerField()
    inteligente = models.IntegerField()
    silenciosa = models.IntegerField()
    autoanulavel = models.IntegerField()
    permitir_inibir = models.IntegerField()
    sirene_intermitente = models.IntegerField()
    chime = models.IntegerField()
    code = models.IntegerField()
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zonas'
