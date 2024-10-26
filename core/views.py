from django.shortcuts import render

# Create your views here.
from .forms import avaliarImcModelForm
from .models import avaliarImc
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

from django.http import HttpResponse
from django.shortcuts import render
from .forms import avaliarImcModelForm  # Certifique-se de que está importando corretamente

def formImc(request):
    print(f'Usuário: {request.user}')
    if str(request.user) != 'AnonymousUser':
        if request.method == 'POST':
            form = avaliarImcModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                form = avaliarImcModelForm()
                return HttpResponse('Dados enviados com sucesso')
            else:
                return HttpResponse('Os Dados não foram enviados')
        else:
            form = avaliarImcModelForm()
        context = {
            'form': form
        }
        return render(request, 'formImc.html', context)
    else:
        return render(request, 'index.html')

def consultaCPF(request):
    context = {
        'pessoa': avaliarImc.objects.all()
    }
    return render(request, 'consultaCPF.html', context)



