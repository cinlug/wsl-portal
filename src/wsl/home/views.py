# coding: utf-8
from django.shortcuts import render_to_response
from django.conf import settings
from wsl.programacao.models import *

def index(request):

	mcs = Minicurso.objects.all()
	minicursos = []
	
	for mc in mcs:
		dic = {}
		dic["titulo"] = mc.titulo
		dic["dia"] = mc.data.day
		dic["mes"] = mc.data.strftime("%b")
		dic["descricao"] = mc.descricao
		dic["foto"] = settings.MEDIA_URL + str(mc.foto)
		
		palestrantes = [p.nome for p in mc.palestrante.all()]
		dic["palestrantes"] = ", ".join(palestrantes)

		minicursos.append(dic)
	
	return render_to_response('index.html', {'minicursos':minicursos})
