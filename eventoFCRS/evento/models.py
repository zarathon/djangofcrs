# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

@python_2_unicode_compatible
class Evento(models.Model):
    nome = models.CharField(max_length=200)
    data = models.DateField()
    local = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    horario = models.TimeField()
    vagas = models.PositiveIntegerField()
    organizador = models.CharField(max_length=200)
    email_organizador = models.EmailField()

    def __str__(self):
        return self.nome


GENERO_CHOICES = [
    ('', 'Gênero'),
    ('MASCULINO', 'Masculino'),
    ('FEMININO', 'Feminino'),
]
ESTADOS_CHOICES = [
    ('', 'UF'),
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MG', 'Minas Gerais'),
    ('MS', 'Mato Grosso do Sul'),
    ('MT', 'Mato Grosso'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('PR', 'Paraná'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('RS', 'Rio Grande do Sul'),
    ('SC', 'Santa Catarina'),
    ('SE', 'Sergipe'),
    ('SP', 'São Paulo'),
    ('TO', 'Tocantins')
]
@python_2_unicode_compatible
class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=200, unique=True)
    genero = models.CharField(max_length=200, choices=GENERO_CHOICES)
    telefone = models.CharField(max_length=200)
    idade = models.PositiveIntegerField()
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=200, choices=ESTADOS_CHOICES)

    def __str__(self):
        return self.nome


class Inscricao(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.evento.nome+" - "+self.usuario.nome
