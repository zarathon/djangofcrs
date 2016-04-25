# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from evento.models import Evento, Usuario, Inscricao
from django.shortcuts import get_object_or_404
from forms import UsuarioForm


def index(request):
    eventos = Evento.objects.all()
    return render(request, 'evento/home.html', {'lista_eventos': eventos})

def mostrar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    return render(request, 'evento/mostrarEvento.html', {'evento': evento})

def inscricao(request, id):
    evento = get_object_or_404(Evento, id=id)
    if request.method == 'POST':
        usuario, created = Usuario.objects.get_or_create(email=request.POST['email'])
        if created:
            usuario.nome = request.POST['nome']
            usuario.cpf = request.POST['cpf']
            usuario.idade = request.POST['idade']
            usuario.cidade = request.POST['cidade']
            usuario.estado = request.POST['estado']
            usuario.genero = request.POST['genero']
            usuario.telefone = request.POST['telefone']
            usuario.save()
        i = Inscricao(evento=evento, usuario=usuario)
        i.save()
        formulario = UsuarioForm()
        return render(request, 'evento/inscricao_form.html', {
            'evento': evento,
            'msg': 'Inscrição realizada com Sucesso!',
            'form': formulario,
            })

    formulario = UsuarioForm()
    return render(request, 'evento/inscricao_form.html', {
        'evento': evento,
        'form': formulario,
        })
