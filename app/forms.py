from django import forms
from .models import (Abastecimentos, Veiculos, TiposAbastecimentos, Funcionarios, Internets, Unidades, Suporteunidades,
					 EntregadoresNormas, PrestadoresNormas, ReservasNormas, MudancasNormas, TatticaFuncionarios, Condominios)


class AbastecimentosForm(forms.ModelForm):
	tattica_veiculo = forms.ModelChoiceField(queryset=Veiculos.objects.all(), label='Nome do Veículo', empty_label=None)
	tipos_abastecimento = forms.ModelChoiceField(queryset=TiposAbastecimentos.objects.all(),
												 label='Tipo de Abastecimento', empty_label=None)
	tattica_funcionario = forms.ModelChoiceField(queryset=Funcionarios.objects.all(), label='Nome do Funcionário',
												 empty_label=None)
	
	class Meta:
		model = Abastecimentos
		fields = [
			'tattica_veiculo', 'tattica_funcionario', 'tipos_abastecimento',
			'data_abastecimento', 'km_atual', 'numero_bloco',
			'qtd_litros', 'total', 'valor_por_litro', 'status'
		]
		widgets = {
			'data_abastecimento': forms.DateInput(attrs={'type': 'date'}),
			'status': forms.NumberInput(attrs={'min': 0, 'max': 10}),
		}

	def __init__(self, *args, **kwargs):
		super(AbastecimentosForm, self).__init__(*args, **kwargs)
		self.fields['tattica_veiculo'].queryset = Veiculos.objects.all()
		self.fields['tattica_funcionario'].queryset = TatticaFuncionarios.objects.all()
		self.fields['tipos_abastecimento'].queryset = TiposAbastecimentos.objects.all()


class CondominiosForm(forms.ModelForm):
    internet = forms.ModelChoiceField(queryset=Internets.objects.none(), label='Nome da Internet', empty_label=None)
    unidade = forms.ModelChoiceField(queryset=Unidades.objects.none(), label='Nome da Unidade', empty_label=None)
    suporteunidade = forms.ModelChoiceField(queryset=Suporteunidades.objects.none(), label='Nome Suporte', empty_label=None)
    entregadores_norma = forms.ModelChoiceField(queryset=EntregadoresNormas.objects.none(), label='Entregadores Normas', empty_label=None)
    prestadores_norma = forms.ModelChoiceField(queryset=PrestadoresNormas.objects.none(), label='Prestadores Normas', empty_label=None)
    reservas_norma = forms.ModelChoiceField(queryset=ReservasNormas.objects.none(), label='Reservas Normas', empty_label=None)
    mudancas_norma = forms.ModelChoiceField(queryset=MudancasNormas.objects.none(), label='Mudanças Normas', empty_label=None)
    responsavel_tattica = forms.ModelChoiceField(queryset=TatticaFuncionarios.objects.none(), label='Nome Funcionario', empty_label=None)

    class Meta:
        model = Condominios
        fields = [
            'internet', 'unidade', 'suporteunidade', 'entregadores_norma', 'prestadores_norma', 'reservas_norma', 'mudancas_norma',
            'responsavel_tattica', 'norma_observacao', 'nome_condominio', 'data_condominio', 'dias_implantacao', 'ramal_condominio',
            'ramal_interno', 'cnpj', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'uf', 'cep', 'website', 'website_agendamento',
            'telefone', 'cameras_usuario'
        ]
        widgets = {
            'data_condominio': forms.DateInput(attrs={'type': 'date'}),
			'status': forms.HiddenInput(),  # Para enviar o valor '1' automaticamente

		}

    def __init__(self, *args, **kwargs):
        super(CondominiosForm, self).__init__(*args, **kwargs)
        self.fields['internet'].queryset = Internets.objects.all()
        self.fields['unidade'].queryset = Unidades.objects.all()
        self.fields['suporteunidade'].queryset = Suporteunidades.objects.all()
        self.fields['entregadores_norma'].queryset = EntregadoresNormas.objects.all()
        self.fields['prestadores_norma'].queryset = PrestadoresNormas.objects.all()
        self.fields['reservas_norma'].queryset = ReservasNormas.objects.all()
        self.fields['mudancas_norma'].queryset = MudancasNormas.objects.all()
        self.fields['responsavel_tattica'].queryset = TatticaFuncionarios.objects.all()
