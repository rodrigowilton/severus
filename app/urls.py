# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('app/', views.index, name='index'),
    path('abastecimentos/new/', views.abastecimento_create, name='abastecimento-create'),
    path('condominios/new/', views.condominio_create, name='condominio-create'),
    path('condominios/', views.condominio_list, name='condominio_list'),
    path('editar_condominio/<int:pk>/', views.editar_condominio, name='editar_condominio'),
    path('consultar_condominio/<int:pk>/', views.consultar_condominio, name='consultar_condominio'),

]
