from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Livro
from .forms import LivroForm

def inicio(request):
    # return HttpResponse("<h1>Boas vindas a livraria Ana Cunha</h1>")
    return render(request, 'pages/inicio.html')

def sobre(request):
    return render(request, 'pages/sobre.html')

def livros(request):
    livros = Livro.objects.all()
    return render(request, 'livros/index.html', {'livros': livros})

def criar(request):
    formulario = LivroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('livros')
    return render(request, 'livros/criar.html', {'formulario': formulario})

def alterar(request, id):
    livro = Livro.objects.get(id=id)
    formulario = LivroForm(request.POST or None, request.FILES or None, instance=livro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('livros')
    return render(request, 'livros/alterar.html', {'formulario': formulario})

def excluir(request, id):
    livro = Livro.objects.get(id=id)
    livro.delete()
    return redirect('livros')

