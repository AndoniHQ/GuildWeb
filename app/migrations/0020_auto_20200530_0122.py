# Generated by Django 2.2.4 on 2020-05-29 23:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20200530_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='Level',
            field=models.IntegerField(default=1, help_text='Introduce el nivel del personaje', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(120)]),
        ),
        migrations.AlterField(
            model_name='character',
            name='Playable_class',
            field=models.CharField(choices=[('1', 'Guerrero'), ('2', 'Paladin'), ('3', 'Cazador'), ('4', 'Picaro'), ('5', 'Sacerdote'), ('7', 'Chaman'), ('8', 'Mago'), ('9', 'Brujo'), ('10', 'Monje'), ('11', 'Druida'), ('12', 'Cazador de demonios'), ('6', 'Caballero de la muerte')], help_text='Introduce la clase del personaje', max_length=2),
        ),
        migrations.AlterField(
            model_name='character',
            name='Realm',
            field=models.CharField(help_text='Introduce el realm del personaje', max_length=20),
        ),
    ]
