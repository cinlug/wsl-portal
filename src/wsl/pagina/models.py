from django.db import models

class Pagina(models.Model):
	titulo   = models.CharField(max_length=200)
	slug     = models.SlugField()
	conteudo = models.TextField()

	def __unicode__(self):
		return self.titulo

# Create your models here.
