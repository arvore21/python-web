from django.shortcuts import render

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
    formulario = LivroForm(request.POST or None)
    return render(request, 'livros/criar.html', {'formulario': formulario})

def alterar(request):
    return render(request, 'livros/alterar.html')

