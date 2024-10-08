# Generated by Django 5.0.6 on 2024-08-18 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='is_persona_fisica_moral',
            field=models.PositiveIntegerField(choices=[(10, 'FISICA'), (20, 'MORAL')], default=10, verbose_name='Persona fisica o moral'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='segundo_nombre',
            field=models.CharField(default='', max_length=150, verbose_name='Segundo nombre (opcional)'),
        ),
    ]
