from django import forms
from .models import agent, Cases

class AgentForm(forms.ModelForm):
    class Meta:
        model = agent
        fields = '__all__'

class CaseForm(forms.ModelForm):
    class Meta:
        model = Cases
        fields = '__all__'