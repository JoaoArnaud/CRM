from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TeamForm
from .models import Team


@login_required
def edit_team(request, pk):
    team = get_object_or_404(Team, created_by=request.user, pk=pk)
    form = TeamForm(instance=team)

    if request.method == "POST":
        form = TeamForm(request.POST, instance=team)

        if form.is_valid():
            form.save()

            messages.success(request, "As alterações foram feitas com sucesso! ✏️")

            return redirect("crmanager:myaccount")

    return render(request, "edit_team.html", {"team": team, "form": form})
