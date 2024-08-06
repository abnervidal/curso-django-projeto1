from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Abner Vidal'
    })

def sobre(request):
    return HttpResponse('Página de Sobre')

def contato(request):
    return HttpResponse('Página de Contato')

# Create your views here.
