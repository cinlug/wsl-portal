from django.db import models
from django.conf import settings

class Palestrante(models.Model):
	nome    = models.CharField(max_length=200)
	slug    = models.SlugField()
	foto    = models.FileField(upload_to='palestrantes', blank=True)
	sobre   = models.TextField()
	email   = models.EmailField()
	twitter = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nome

class Prerequisito(models.Model):
	titulo = models.CharField(max_length=100)
	descricao = models.TextField()

	def __unicode__(self):
		return self.titulo

class Minicurso(models.Model):
	titulo          = models.CharField(max_length=200)
	slug            = models.SlugField()
	
	#foto	        = models.FileField(upload_to='minicursos')
	descricao       = models.TextField()

	data            = models.DateField()
	hora_inicio     = models.TimeField()
	hora_fim        = models.TimeField()

	palestrante = models.ManyToManyField(Palestrante, null=True, blank=True)
	prerequisitos = models.ManyToManyField(Prerequisito, null=True, blank=True)

	def __unicode__(self):
		return self.titulo

