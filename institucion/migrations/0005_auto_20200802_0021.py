# Generated by Django 3.0.8 on 2020-08-02 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institucion', '0004_auto_20200802_0003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='institucion',
            old_name='gerente',
            new_name='rector',
        ),
    ]