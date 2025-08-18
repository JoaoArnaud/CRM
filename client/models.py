from django.db import models
from django.contrib.auth.models import User

from team.models import Team


class Client(models.Model):
    # Novas opções para Tipo de Serviço
    OPEN = "open"
    CONT = "cont"
    ENDING = "ending"
    CHANGING = "changing"
    SN = "sn"
    FOLHA = "folha"
    EMISSAO = "emissao"
    CONSUL = "consul"
    PLAN = "plan"
    OTHER = "other"

    CHOICES_SERVICE_TYPE = (
        (OPEN, "Abertura de empresa"),
        (CONT, "Contabilidade"),
        (ENDING, "Encerramento de empresa"),
        (CHANGING, "Troca de contador"),
        (SN, "Regularização no Simples Nacional"),
        (FOLHA, "Folha de pagamento"),
        (EMISSAO, "Emissão de notas fiscais"),
        (CONSUL, "Consultoria fiscal ou tributária"),
        (PLAN, "Planejamento tributário"),
        (OTHER, "Outro"),
    )

    # Campos principais
    team = models.ForeignKey(Team, related_name="leads", on_delete=models.CASCADE)
    name = models.CharField("Nome do cliente", max_length=255)
    email = models.EmailField("E-mail")
    phone = models.CharField("Telefone", max_length=20, blank=True, null=True)
    company_name = models.CharField(
        "Nome da empresa", max_length=255, blank=True, null=True
    )
    cnpj = models.CharField("CNPJ", max_length=18, blank=True, null=True)
    service_type = models.CharField(
        "Tipo de serviço",
        max_length=30,
        choices=CHOICES_SERVICE_TYPE,
        blank=True,
        null=True,
    )
    description = models.TextField(blank=True, null=True)

    # Metadata
    created_by = models.ForeignKey(
        User, related_name="clients", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    modified_at = models.DateTimeField("Atualizado em", auto_now=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name
