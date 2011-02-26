from django.shortcuts import render_to_response
from wsl.pagina.models import Pagina

def index(request, url):
	pgs = Pagina.objects.filter(slug=url)

	if pgs:
		pagina = pgs[0]
		return render_to_response('pagina.html', {'pagina':pagina})

	return render_to_response('index.html')
