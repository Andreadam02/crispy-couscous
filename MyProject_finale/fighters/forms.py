# forms.py
from django import forms
from .models import Fighter

class FighterForm(forms.ModelForm):
    class Meta:
        model = Fighter
        fields = ['nome', 'descrizione']  # Elenco dei campi che desideri inserire