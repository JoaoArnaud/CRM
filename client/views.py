from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Client
from .forms import AddClientForm

@login_required
def clients(request):
    clients = Client.objects.filter(created_by=request.user)
    return render(request, 'clients.html', {
        'clients':clients
    })

@login_required
def clients_detail(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)
    return render(request, 'clients_detail.html', {
        'client':client
    })

@login_required
def add_client(request):
    if request.method == 'POST':
        form = AddClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.created_by = request.user
            client.save()

            messages.success(request, 'Cliente criado com sucesso! ✅')

            return redirect('client:clients')
    else:
        form = AddClientForm()

    form = AddClientForm
    return render(request, 'add_client.html', {
        'form': form
   })

@login_required
def client_delete(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)
    client.delete()

    messages.success(request, 'Cliente excluído com sucesso! 👋')

    return redirect('client:clients')

@login_required
def client_edit(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)

    if request.method == 'POST':
        form = AddClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, 'Alterações salvas com sucesso! ✒️')
            return redirect('client:clients')
    else:
        form = AddClientForm(instance=client)
    return render(request, 'edit_client.html', {
        'form': form
    })