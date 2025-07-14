# CRManager/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home.html')

# Você pode adicionar outras views do CRM aqui, também protegidas com @login_required
# def clientes(request):
#     return render(request, 'CRManager/clientes.html')