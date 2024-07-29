from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class Usuario(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('self',  # Point to itself
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='created_usuarios'  # Add related_name here
    )
    updated_by = models.ForeignKey('self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='updated_usuarios'  # Add related_name here
    )
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuarios',  # Add related_name here
        blank=True,
        help_text=_("The groups this user belongs to. A user may belong to multiple groups. A group typically includes permissions to perform specific operations."),
        verbose_name=_("Groups"),
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuarios',  # Add related_name here
        blank=True,
        help_text=_("Specific permissions for this user."),
        verbose_name=_("User Permissions"),
    )
