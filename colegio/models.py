from django.db import models
from usuario.models import Usuario 

from django.db import models

class Colegio(models.Model):
    nombre_escuela = models.CharField(max_length=200, null=False, blank=False)
    clave_escolar = models.CharField(max_length=200,null=False, blank=False)
    representante = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='colegio/logo/')
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20,null=False, blank=False)
    email = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.SET_NULL, related_name='created_colegio')
    updated_by = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.SET_NULL, related_name='updated_colegio')

    def __str__(self):
        return self.nombre_escuela

class Ciclo(models.Model):
    colegio = models.ForeignKey(Colegio, on_delete=models.CASCADE, related_name='ciclos')
    date_start = models.DateField(null=False, blank=False)
    date_end = models.DateField(null=False, blank=False)
    descripcion = models.TextField(null=True, blank=True)
    year_start = models.IntegerField(null=False, blank=True)
    year_end = models.IntegerField(null=False, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.SET_NULL, related_name='created_ciclo')
    updated_by = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.SET_NULL, related_name='updated_ciclo')

    def __str__(self):
        return f"Ciclo {self.year_start} - {self.year_end}"
    
    
class NivelEscolar(models.Model):
    nombre = models.CharField(max_length=200,null=False, blank=False)
    descripcion = models.TextField(null=True, blank=True)

    #colegio = models.ForeignKey(Colegio, on_delete=models.CASCADE, related_name='niveles')
    #ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE, related_name='niveles', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.SET_NULL, related_name='created_nivel')
    updated_by = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.SET_NULL, related_name='updated_nivel')

    def __str__(self):
        return self.nombres
    


class Seccion(models.Model):
    nombre = models.CharField(max_length=200, null=False, blank=False)
    descripcion = models.TextField(null=True, blank=True)
    hora_inicio = models.TimeField(null=False, blank=False)
    hora_fin = models.TimeField(null=False, blank=False)
    minutos_clase = models.IntegerField(null=False, blank=False)
    nota = models.TextField(null=True, blank=True)
    nivel = models.ForeignKey('NivelEscolar', on_delete=models.CASCADE, related_name='secciones')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.SET_NULL, related_name='created_seccion')
    updated_by = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.SET_NULL, related_name='updated_seccion')
    
    def __str__(self):
        return f'{self.nombre} {self.nivel.nombre}'

