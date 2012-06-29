#encoding:utf-8
from django.forms import ModelForm
from django import forms
from principal.models import Curso, Cuestionario
'''
class ContactoForm(forms.Form):
	correo = forms.EmailField(label='Tu correo-e')
	mensaje = forms.CharField(widget=forms.Textarea)

class ComentarioForm(ModelForm):
	class Meta:
		model = Comentario

'''
class CursoForm(ModelForm):
	class Meta:
		model = Curso

