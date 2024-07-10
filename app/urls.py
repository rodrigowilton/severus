from django.urls import path
from . import views
from .views import abastecimento_create, condominio_create, condominio_list

urlpatterns = [
	path('app/', views.index, name='index'),
	path('abastecimentos/new/', abastecimento_create, name='abastecimento-create'),
	path('condominios/new/', condominio_create, name='condominio-create'),
	path('condominios/', condominio_list, name='condominio_list'),

]
