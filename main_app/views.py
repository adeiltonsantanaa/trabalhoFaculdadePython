from django.shortcuts import render, get_object_or_404, redirect
from .forms import URLForm
from .models import EnderecoWeb
import requests

def home(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        EnderecoWeb.objects.create(url=url)
        return redirect('lista_enderecos')

    return render(request, 'main_app/home.html')

def lista_enderecos(request):
    enderecos = EnderecoWeb.objects.all()
    return render(request, 'main_app/lista_enderecos.html', {'enderecos': enderecos})

def excluir_endereco(request, pk):
    endereco = EnderecoWeb.objects.get(pk=pk)

    if request.method == 'POST':
        endereco.delete()
        return redirect('lista_enderecos')

    return render(request, 'main_app/excluir_endereco.html', {'endereco': endereco})

def alterar_url(request, pk):
    endereco = get_object_or_404(EnderecoWeb, pk=pk)
    if request.method == 'POST':
        form = URLForm(request.POST, instance=endereco)
        if form.is_valid():
            form.save()
            return redirect('lista_enderecos')
    else:
        form = URLForm(instance=endereco)
    return render(request, 'main_app/alterar_url.html', {'form': form, 'pk': pk})

def verificar_url(request, pk):
    if request.method == 'POST':
        endereco = get_object_or_404(EnderecoWeb, pk=pk)
        try:
            response = requests.get(endereco.url)
            if response.status_code == 200:
                validacao = '🟢'
            else:
                validacao = '🔴'
        except requests.exceptions.RequestException as err:
            validacao = '🔴'

        endereco.validacao = validacao
        endereco.save()

        return redirect('lista_enderecos')
