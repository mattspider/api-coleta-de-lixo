from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models



class Infanunciante(models.Model):



    nome = models.CharField(null=True, default=0,max_length=55)
    cpf = models.CharField(null=True, default=0,max_length=55)
    email = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"CPF:{self.cpf} NOME:f{self.nome} "

    class Meta:
        verbose_name_plural = "Infanunciante"



class anuncios(models.Model):



    usuario = models.CharField(max_length=255)
    numero = models.CharField(null=True, default=0, max_length=255)
    logradouro = models.CharField(max_length=255)
    nome_da_rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255,null=True, blank=True)
    desc = models.CharField(max_length=255, null=True, blank=True)
    seg = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Usuario:{self.usuario}\nTipo:{self.tipo}"

    class Meta:
        verbose_name_plural = "Anuncio"

class Infempresa(models.Model):    
    nome = models.CharField(max_length=255, null=True)
    cnpj = models.CharField(null=True, default=0,max_length=18)
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    numero = models.CharField(null=True, default=0,max_length=255)
    email = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"CNPJ:{self.cnpj}"

    class Meta:
        verbose_name_plural = "Infempresa"
        



