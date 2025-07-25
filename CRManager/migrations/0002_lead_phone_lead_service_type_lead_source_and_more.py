# Generated by Django 5.2.4 on 2025-07-23 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRManager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='service_type',
            field=models.CharField(blank=True, choices=[('open', 'Abertura de empresa'), ('cont', 'Contabilidade'), ('ending', 'Encerramento de empresa'), ('changing', 'Troca de contador'), ('sn', 'Regularização no Simples Nacional'), ('folha', 'Folha de pagamento'), ('emissao', 'Emissão de notas fiscais'), ('consul', 'Consultoria fiscal ou tributária'), ('plan', 'Planejamento tributário'), ('other', 'Outro')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='source',
            field=models.CharField(choices=[('website', 'Google / Site'), ('referral', 'Indicação'), ('social_media', 'Mídia Social'), ('ads', 'Anúncio pago (Ads)'), ('event', 'Evento'), ('other', 'Outro')], default='other', max_length=20),
        ),
        migrations.AlterField(
            model_name='lead',
            name='status',
            field=models.CharField(choices=[('new', 'Novo'), ('contacted', 'Contatado'), ('won', 'Ganho'), ('lost', 'Perdido')], default='new', max_length=10),
        ),
    ]
