from django.db import models
from django.contrib.auth.models import User

class Lead(models.Model):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

    CHOICES_PRIORITY = (
        (LOW, 'Pequena'),
        (MEDIUM, 'Média'),
        (HIGH, 'Alta'),
    )

    NEW = 'new'
    CONTACTED = 'contacted'
    WON = 'won'
    LOST = 'lost'

    CHOICES_STATUS = (
        (NEW, 'Novo'),
        (CONTACTED, 'Contatado'),
        (WON, 'Ganho'),
        (LOST, 'Perdido'),
    )

    # Novas opções para Origem
    WEBSITE = 'website'
    REFERRAL = 'referral'
    SOCIAL_MEDIA = 'social_media'
    ADS = 'ads'
    EVENT = 'event'
    OTHER = 'other'

    CHOICES_SOURCE = (
        (WEBSITE, 'Google / Site'),
        (REFERRAL, 'Indicação'),
        (SOCIAL_MEDIA, 'Mídia Social'),
        (ADS, 'Anúncio pago (Ads)'),
        (EVENT, 'Evento'),
        (OTHER, 'Outro'),
    )

    # Novas opções para Tipo de Serviço
    OPEN = "open"
    CONT = "cont"
    ENDING = "ending"
    CHANGING = "changing"
    SN = 'sn'
    FOLHA = 'folha'
    EMISSAO = 'emissao'
    CONSUL = 'consul'
    PLAN = 'plan'
    OTHER = 'other'

    CHOICES_SERVICE_TYPE = (
        (OPEN, 'Abertura de empresa'),
        (CONT, 'Contabilidade'),
        (ENDING, 'Encerramento de empresa'),
        (CHANGING, 'Troca de contador'),
        (SN, 'Regularização no Simples Nacional'),
        (FOLHA, 'Folha de pagamento'),
        (EMISSAO, 'Emissão de notas fiscais'),
        (CONSUL, 'Consultoria fiscal ou tributária'),
        (PLAN, 'Planejamento tributário'),
        (OTHER, 'Outro'),
    )

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=10, choices=CHOICES_PRIORITY, default=MEDIUM)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=NEW)
    source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default=OTHER)
    service_type = models.CharField(max_length=20, choices=CHOICES_SERVICE_TYPE, blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='leads', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    converted_to_client = models.BooleanField(default=False)

    def __str__(self):
        return self.name