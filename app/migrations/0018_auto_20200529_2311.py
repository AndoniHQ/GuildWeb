# Generated by Django 2.2.4 on 2020-05-29 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20200529_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='Playable_race',
            field=models.CharField(blank=True, choices=[('1', 'Humano'), ('2', 'Orco'), ('3', 'Enano'), ('4', 'Elfo de la noche'), ('5', 'No-muerto'), ('6', 'Tauren'), ('7', 'Gnomo'), ('8', 'Troll'), ('9', 'Duende'), ('10', 'Elfo de sangre'), ('11', 'Draenei'), ('12', 'Orco equivocado'), ('13', 'Continuar'), ('14', 'Roto'), ('15', 'Esqueleto'), ('16', 'Vrykul'), ('17', 'Tuskarr'), ('18', 'Trol del bosque'), ('19', 'Tono'), ('20', 'Esqueleto de Rasganorte'), ('21', 'Troll de hielo'), ('22', 'Huargen'), ('23', 'Gilnean'), ('24', 'Pandaren'), ('25', 'Pandaren'), ('26', 'Pandaren'), ('27', 'Noche'), ('28', 'Tauren de montaña alta'), ('29', 'Elfo vacío'), ('30', 'Draenei forjado por la luz'), ('31', 'Troll Zandalari'), ('32', 'Kul Tiran'), ('33', 'Humano'), ('34', 'Enano hierro negro'), ('35', 'Vulpera'), ('36', 'Orco Maghar'), ('37', 'Mecagnomo')], help_text='Introduce la raza del personaje', max_length=2),
        ),
    ]
