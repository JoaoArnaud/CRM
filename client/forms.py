from django import forms

from .models import Client


class AddClientForm(forms.ModelForm):
    class Meta:
        model = Client
        # Including fields present in the Client model and requested in the form
        fields = (
            "name",
            "email",
            "phone",
            "company_name",
            "cnpj",
            "service_type",
            "description",
        )
        labels = {
            "name": "Nome do Cliente",  # Adjusted to be more specific
            "email": "E-mail",
            "phone": "Telefone",
            "company_name": "Nome da Empresa",  # Added label for company_name
            "cnpj": "CNPJ",  # Added label for CNPJ
            "service_type": "Tipo de Serviço Contratado",
            "description": "Descrição",
        }
