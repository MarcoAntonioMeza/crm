from django.db import models
from usuario.models import Usuario  # Importa tu modelo de usuario personalizado

from django.contrib.auth import get_user_model
from django.utils import timezone
from auditlog.registry import auditlog

User = get_user_model()

class Cliente(models.Model):
    PERSONA_FISICA = 10
    PERSONA_MORAL = 20
    
    PERSONA_CHOICES = [
        (PERSONA_FISICA, 'FISICA'),
        (PERSONA_MORAL, 'MORAL')
    ]
    
    nombre = models.CharField(max_length=150)
    segundo_nombre = models.CharField(max_length=150, default="",verbose_name='Segundo nombre (opcional)')
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    is_persona_fisica_moral = models.PositiveIntegerField(choices=PERSONA_CHOICES, default=PERSONA_FISICA,
                                                        verbose_name='Persona fisica o moral')
    numero = models.CharField(max_length=11)
    segundo_numero = models.CharField(max_length=11, default=None)
    correo = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    created_by = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.SET_NULL, related_name='created_clients')
    updated_by = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.SET_NULL, related_name='updated_clients')
    


    def save(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Extrae el usuario de kwargs, si está presente
        if self.pk:  # Si ya existe una instancia (es una actualización)
            
            if user and isinstance(user, User):
                self.updated_by = user
        else:  # Si es una nueva instancia
            
            if user and isinstance(user, User):
                self.created_by = user
        super(Cliente, self).save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.nombre} {self.segundo_nombre} {self.apellido_paterno} {self.apellido_materno}'


auditlog.register(Cliente)