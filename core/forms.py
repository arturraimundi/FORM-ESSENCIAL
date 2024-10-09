from django import forms

from .models import avaliarImc

class avaliarImcModelForm(forms.ModelForm):
    class Meta:
        model = avaliarImc
        fields = ['cpf', 'nome', 'sexo', 'data_nascimento', 'escola', 'peso', 'altura', 'foto']