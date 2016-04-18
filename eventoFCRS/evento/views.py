from django.shortcuts import render
from django.http import HttpResponse
from evento.models import Evento
from django.shortcuts import get_object_or_404

def index(request):
    eventos = Evento.objects.all()
    return render(request, 'evento/home.html', {'lista_eventos': eventos})

def mostrar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    return render(request, 'evento/mostrarEvento.html', {'evento': evento})
