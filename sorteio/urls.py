from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "sorteio"

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('sorteio_time/', views.sorteio_time, name='sorteio_time'),
    path('sobre_mim/', views.sobre_mim, name='sobre_mim'),
    path('sorteio_time/resultado/', views.resultado_time, name='resultado_time'),
    path('mostrar_erro/', views.mostrar_erro, name='mostrar_erro'),
    path('contar_linhas/', views.contar_linhas, name='contar_linhas'),
    path('sorteio_nome/', views.sorteio_nome, name='sorteio_nome'),
    path('resultado_nome/', views.resultado_nome, name='resultado_nome'),
]

