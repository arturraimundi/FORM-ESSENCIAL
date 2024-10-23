from django.shortcuts import render

# Create your views here.
from .forms import avaliarImcModelForm
from .models import avaliarImc
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def formImc(request):
    if request.method == 'POST':
        form = avaliarImcModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = avaliarImcModelForm()
            #messages.success(request, 'Produto Salvo com sucesso.')
            return HttpResponse('Dados enviados com sucesso')
            
        else:
            #messages.error(request, 'Erro ao salvar o produto')
            return HttpResponse('Os Dados não foram enviados')
    else:
        form = avaliarImcModelForm()
    context = {
        'form': form
    }
    return render(request, 'formImc.html', context)
def consultaCPF(request):
    context = {
        'pessoa': avaliarImc.objects.all()
    }
    return render(request, 'consultaCPF.html', context)



