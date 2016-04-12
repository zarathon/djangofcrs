from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'evento/home.html', {
        'nome': "Zarathon Maia",
        'idade': '30 anos',
        'altura': '1,92 metros',
        })
