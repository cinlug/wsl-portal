from django.shortcuts import render_to_response
from wsl.programacao.models import Minicurso, Palestrante

def index(request):
	return render_to_response('index.html')

def minicurso(request, mc):
	mcs = Minicurso.objects.filter(slug=mc)
	
	if mcs:
		curso = mcs[0]
		palestrantes = curso.palestrante.all()
		return render_to_response('minicurso.html', {'mc':curso, 'palestrantes':palestrantes})
	else:
		return render_to_response('index.html')

def palestrante(request, palestrante):
	pls = Palestrante.objects.filter(slug=palestrante)

	if pls:
		palestrante = pls[0]
		return render_to_response('palestrante.html', {'palestrante':palestrante})
	
	return render_to_response('index.html')
