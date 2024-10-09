from django.db import models

# Create your models here.
from django.db import models

from stdimage.models import StdImageField
#CPF chave primaria, valor não nulo, valor único
#Nome valor não nulo
#Sexo valor não nulo
#Data de Nascimento valor não nulo
#Escola valor não nulo
#Peso (Na unidade kg) valor não nulo
#Altura (Altura em metros) valor não nulo
#foto (foto da pessoa avaliada) valor não nulo
class avaliarImc(models.Model):
    SEXO_CHOICES = (
        ("1", "Feminino"),
        ("2", "Masculino"),
        ("3", "Não Binário"),
        ("4", "outro"),
        ("5","Prefiro não dizer"),
    )
        
    cpf = models.IntegerField('CPF', primary_key=True, unique=True, null=False)
    nome = models.CharField('Nome', max_length=100, null=False)
    sexo = models.CharField('Sexo', max_length=3, choices=SEXO_CHOICES, blank=False, null=False)
    data_nascimento = models.DateField("data de nascimento", null=False)
    escola = models.CharField('Escola', max_length=100, null=False)
    peso = models.DecimalField('Peso em kg', max_digits=5, decimal_places=2,  null=False)
    altura = models.DecimalField('Altura em metros', max_digits=5, decimal_places=2, null=False)
    foto = StdImageField('foto da pessoa avaliada', upload_to='avaliados', variations={'thumb':(125,125)}, null=False)

    def __str__(self):
        return self.nome