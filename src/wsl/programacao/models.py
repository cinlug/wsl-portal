from django.db import models

class Palestrante(models.Model):
	nome    = models.CharField(max_length=200)
	sobre   = models.TextField()
	email   = models.EmailField()
	twitter = models.CharField(max_length=100)

class Palestra(models.Model):
	titulo    = models.CharField(max_length=200)
	slug      = models.SlugField()
	descricao = models.TextField()

	data      = models.DateField()
	hora      = models.TimeField()

	palestrante = models.ManyToManyField(Palestrante)

