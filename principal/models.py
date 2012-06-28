#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
	curso_id = models.AutoField(primary_key=True)
	nombre_curso = models.TextField()

	def __unicode__(self):
		return self.nombre_curso

class Cuestionario(models.Model):
	cuestionario_id = models.AutoField(primary_key=True)
	nombre_cuestionario = models.TextField()

	def __unicode__(self):
		return self.nombre_cuestionario

class Grupo(models.Model):		
	grupo_id = models.AutoField(primary_key=True)
	nombre_grupo = models.TextField()
	fecha = models.DateTimeField()
	curso = models.ForeignKey(Curso)
	cuestionario = models.ForeignKey(Cuestionario)
	usuario = models.ForeignKey(User)

	def __unicode__(self):
		return self.nombre_grupo

class Participante(models.Model):
	participante_id = models.AutoField(primary_key=True)
	nombre = models.TextField()

	def __unicode__(self):
		return self.nombre

class DetalleGrupo(models.Model):
	grupo = models.ForeignKey(Grupo)
	participante = models.ForeignKey(Participante)
	nombre = models.TextField()
	usuario = models.ForeignKey(User)
	fregistro = models.DateTimeField(auto_now=True)
	
