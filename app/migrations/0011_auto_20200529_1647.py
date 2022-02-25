# Generated by Django 2.2.4 on 2020-05-29 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20200529_0139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='Class',
        ),
        migrations.RemoveField(
            model_name='character',
            name='Rol',
        ),
        migrations.RemoveField(
            model_name='character',
            name='User',
        ),
        migrations.AddField(
            model_name='character',
            name='Level',
            field=models.IntegerField(default=0, help_text='Introduce el nivel del personaje'),
        ),
        migrations.AddField(
            model_name='character',
            name='Playable_class',
            field=models.CharField(blank=True, help_text='Introduce la clase del personaje', max_length=20),
        ),
        migrations.AddField(
            model_name='character',
            name='Playable_race',
            field=models.CharField(blank=True, help_text='Introduce la raza del personaje', max_length=20),
        ),
        migrations.AddField(
            model_name='character',
            name='Playable_spec',
            field=models.CharField(blank=True, help_text='Introduce la especializacion del personaje', max_length=20),
        ),
        migrations.AddField(
            model_name='character',
            name='Rank',
            field=models.IntegerField(default=0, help_text='Introduce el rango del personaje'),
        ),
        migrations.AddField(
            model_name='character',
            name='Realm',
            field=models.CharField(blank=True, help_text='Introduce el realm del personaje', max_length=20),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]