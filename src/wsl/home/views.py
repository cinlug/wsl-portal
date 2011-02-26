# coding: utf-8
from django.shortcuts import render_to_response
from django.conf import settings
from wsl.programacao.models import *

def index(request):
	return render_to_response('index.html')
