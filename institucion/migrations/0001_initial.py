# Generated by Django 3.0.8 on 2020-07-26 01:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre de su empresa.', max_length=50)),
                ('slogan', models.TextField(blank=True, help_text='Frase Slogan de su negocio.', null=True)),
                ('descripcion', models.TextField(blank=True, help_text='Describa el campo ocupacional y área de su empresa.', null=True)),
                ('direccion', models.CharField(max_length=150, null=True)),
                ('telefono', models.CharField(max_length=20, null=True)),
                ('sitio_web', models.URLField(blank=True, help_text='Página web de su empresa.', null=True)),
                ('gerente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Institucion',
                'verbose_name_plural': 'Instituciones',
            },
        ),
    ]
