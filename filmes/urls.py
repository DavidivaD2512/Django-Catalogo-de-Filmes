from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_filmes, name='lista_filmes'),
    path('novo/', views.criar_filme, name='criar_filme'),
    path('editar/<int:pk>', views.atualizar_filme, name='atualizar_filme'),
    path('deletar/<int:pk>', views.deletar_filme, name='deletar_filme'),
]
