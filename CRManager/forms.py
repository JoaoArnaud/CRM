from django import forms
from .models import Lead
class AddLeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ('name', 'email', 'description', 'priority', 'status')
        labels = {
            'name': 'Nome',
            'email': 'E-mail',
            'description': 'Descrição',
            'priority': 'Prioridade',
            'status': 'Status',
        }