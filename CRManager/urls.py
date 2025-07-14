from django.urls import path
from . import views

app_name = 'crmanager' # Define um namespace para suas URLs do CRM

urlpatterns = [
    path('home/', views.home, name='home'),
    # Adicione outras URLs do seu CRM aqui
    # path('clientes/', views.clientes, name='clientes'),
]