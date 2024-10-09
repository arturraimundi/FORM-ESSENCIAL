from django.contrib import admin

# Register your models here.

from .models import avaliarImc

@admin.register(avaliarImc)

class avaliarImcAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'nome', 'sexo', 'data_nascimento', 'escola', 'peso', 'altura', 'foto')


