#encoding:utf-8
from principal.models import Curso, Cuestionario
from principal.forms import CursoForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

def cursos(request):
	cursos = Curso.objects.all()
	return render_to_response('cursos.html', {'datos':cursos}, context_instance=RequestContext(request))

def nuevo_curso(request):
	if request.method == 'POST':
		formulario = CursoForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/cursos')
	else:
		formulario = CursoForm()
	return render_to_response('cursoform.html', {'formulario':formulario, 'butonDelete':0}, context_instance=RequestContext(request))

def curso(request, curso_id):
	if request.method == 'POST':
		curso = get_object_or_404(Curso, pk=curso_id)
		formulario = CursoForm(request.POST, instance=curso)
		if request.POST.get('Registrar'):			
			if formulario.is_valid():
				formulario.save()
				return HttpResponseRedirect('/cursos')
		if request.POST.get('Eliminar'):
			curso.delete()
			return HttpResponseRedirect('/cursos')
	else:
		curso = get_object_or_404(Curso, pk=curso_id)	
		formulario = CursoForm(instance=curso)
	return render_to_response('cursoform.html', {'formulario':formulario, 'butonDelete':1}, context_instance=RequestContext(request))



