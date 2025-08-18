from django import forms
from .models import Lead


class AddLeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        # Adicione 'phone', 'source' e 'service_type' aqui
        fields = (
            "name",
            "email",
            "phone",
            "description",
            "priority",
            "status",
            "source",
            "service_type",
        )
        labels = {
            "name": "Nome",
            "email": "E-mail",
            "phone": "Telefone",  # Novo label
            "description": "Descrição",
            "priority": "Prioridade",
            "status": "Status",
            "source": "Origem",  # Novo label
            "service_type": "Tipo de Serviço Desejado",  # Novo label
        }
