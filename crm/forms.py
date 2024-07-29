from django import forms
from .models import Cliente  # Asegúrate de que la ruta al modelo sea correcta
from usuario.models import Usuario
from django.contrib.auth import get_user_model

User = get_user_model()


"""
=======================================================
                FORMULARIO CLIENTE
=======================================================
"""
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nombre',
            'segundo_nombre',
            'apellido_paterno',
            'apellido_materno',
            'is_persona_fisica_moral',
            'numero',
            'segundo_numero',
            'correo',
            'avatar'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control text-lead'}),
            'segundo_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_materno': forms.TextInput(attrs={'class': 'form-control'}),
            'is_persona_fisica_moral': forms.Select(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'segundo_numero': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }



    def save(self, commit=True, *args, **kwargs):
        usuario = kwargs.pop('user', None)  # Extrae el usuario de kwargs, si está presente
        instance = super().save(commit=False)
        if usuario and isinstance(usuario, User):
            if not instance.pk:
                instance.created_by = usuario
            instance.updated_by = usuario
        if commit:
            instance.save(user=usuario)
        return instance