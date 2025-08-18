# CRManager/views.py
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from client.models import Client
from team.models import Team

from .forms import AddLeadForm
from .models import Lead


@login_required
def leads_delete(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    lead.delete()

    messages.success(request, "Lead deletada com sucesso! 👋")

    return redirect("crmanager:leads")


@login_required
def leads_edit(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)

    if request.method == "POST":
        form = AddLeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            messages.success(request, "Alterações salvas com sucesso! ✒️")
            return redirect("crmanager:leads")
    else:
        form = AddLeadForm(instance=lead)
    return render(request, "leads_edit.html", {"form": form})


@login_required
def home(request):
    team = Team.objects.filter(created_by=request.user)[0]

    leads = Lead.objects.filter(team=team, converted_to_client=False).order_by(
        "-created_at"
    )[0:5]
    clients = Client.objects.filter(team=team).order_by("-created_at")[0:5]

    return render(request, "home.html", {"leads": leads, "clients": clients})


@login_required
def leads_detail(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    return render(request, "leads_detail.html", {"lead": lead})


@login_required
def leads(request):
    leads = Lead.objects.filter(created_by=request.user, converted_to_client=False)
    return render(request, "leads.html", {"leads": leads})


@login_required
def add_lead(request):
    if request.method == "POST":
        form = AddLeadForm(request.POST)
        if form.is_valid():
            team = Team.objects.filter(created_by=request.user)[0]
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.team = team
            lead.save()

            messages.success(request, "Lead criada com sucesso! ✅")

            return redirect("crmanager:leads")
    else:
        form = AddLeadForm()

    form = AddLeadForm
    return render(request, "add_lead.html", {"form": form})


@login_required
def convert_to_client(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    team = Team.objects.filter(created_by=request.user)[0]

    client = Client.objects.create(
        name=lead.name,
        email=lead.email,
        phone=lead.phone,
        service_type=lead.service_type,
        description=lead.description,
        created_by=request.user,
        team=team,
    )

    lead.converted_to_client = True
    lead.save()

    messages.success(request, "Lead convertida em cliente com sucesso, parabéns! 🎉")
    return redirect("crmanager:leads")


@login_required
def myaccount(request):
    team = Team.objects.filter(created_by=request.user)[0]
    return render(request, "myaccount.html", {"team": team})
