#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
	curso_id = models.AutoField(primary_key=True)
	nombre_curso = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre_curso

class Cuestionario(models.Model):
	cuestionario_id = models.AutoField(primary_key=True)
	nombre_cuestionario = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre_cuestionario

class Grupo(models.Model):		
	grupo_id = models.AutoField(primary_key=True)
	nombre_grupo = models.CharField(max_length=100)
	fecha = models.DateTimeField()
	curso = models.ForeignKey(Curso)
	cuestionario = models.ForeignKey(Cuestionario)
	usuario = models.ForeignKey(User)

	def __unicode__(self):
		return self.nombre_grupo

class Participante(models.Model):
	participante_id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=300)

	def __unicode__(self):
		return self.nombre

class DetalleGrupo(models.Model):
	grupo = models.ForeignKey(Grupo)
	participante = models.ForeignKey(Participante)
	usuario = models.ForeignKey(User)
	fregistro = models.DateTimeField(auto_now=True)
	
