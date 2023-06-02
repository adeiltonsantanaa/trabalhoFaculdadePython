from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('enderecos/', views.lista_enderecos, name='lista_enderecos'),
    path('enderecos/excluir/<int:pk>/', views.excluir_endereco, name='excluir_endereco'),
    path('alterar/<int:pk>/', views.alterar_url, name='alterar_url'),
    path('verificar_url/<int:pk>', views.verificar_url, name='verificar_url'),
    path('verificar_urls/', views.verificar_urls, name='verificar_urls')
]
