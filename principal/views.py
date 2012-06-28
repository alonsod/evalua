#encoding:utf-8
from principal.models import Curso, Cuestionario
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def cursos(request):
	cursos = Curso.objects.all()
	return render_to_response('cursos.html', {'datos':cursos}, context_instance=RequestContext(request))

