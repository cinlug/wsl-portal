from django.db import models
from django.conf import settings

class Palestrante(models.Model):
	nome    = models.CharField(max_length=200)
	sobre   = models.TextField()
	email   = models.EmailField()
	foto    = models.CharField(max_length=200)
	twitter = models.CharField(max_length=100)

class Palestra(models.Model):
	titulo          = models.CharField(max_length=200)
	slug            = models.SlugField()
	
	foto	        = models.FileField(upload_to='minicursos')
	descricao       = models.TextField()
	descricao_longa = models.TextField()

	data      = models.DateField()
	hora      = models.TimeField()

	palestrante = models.ManyToManyField(Palestrante)

class Prerequisito(models.Model):
	titulo = models.CharField(max_length=100)
	descricao = models.CharField(max_length=250)

class Minicurso(Palestra):
	prerequisitos = models.ManyToManyField(Prerequisito)
