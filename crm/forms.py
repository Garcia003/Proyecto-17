from tkinter import Widget
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

    def __init__(self, *args, **kwargs):
        super(CaseForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'input'})