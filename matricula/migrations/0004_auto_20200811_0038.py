# Generated by Django 3.0.8 on 2020-08-11 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0003_solicitudingreso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudingreso',
            name='tipo_matricula',
            field=models.CharField(choices=[(1, 'ORDINARIA'), (2, 'EXTRAORDINARIA')], default='2', max_length=50),
        ),
    ]