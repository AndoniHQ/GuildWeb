import json
import requests
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

client_id = '2a3f57b9e9ca493b9caafdd338853adb'
client_secret = 'aLb4rNxxs2snC8t77vC45gsumqh7yKdK'


class Character(models.Model):
    """
    Clase que define los personajes de los usuarios
    """

    Name = models.CharField(
        max_length=20, help_text="Introduce el nombre del personaje", primary_key=True)

    Realm = models.CharField(
        max_length=20, help_text="Introduce el realm del personaje")

    p_class_choices = [
        ('1', 'Guerrero'),
        ('2', 'Paladin'),
        ('3', 'Cazador'),
        ('4', 'Picaro'),
        ('5', 'Sacerdote'),
        ('7', 'Chaman'),
        ('8', 'Mago'),
        ('9', 'Brujo'),
        ('10', 'Monje'),
        ('11', 'Druida'),
        ('12', 'Cazador de demonios'),
        ('6', 'Caballero de la muerte'),
    ]
    Playable_class = models.CharField(
        max_length=2, choices=p_class_choices, help_text="Introduce la clase del personaje")

    p_race_choices = [
        ('1', 'Humano'),
        ('2', 'Orco'),
        ('3', 'Enano'),
        ('4', 'Elfo de la noche'),
        ('5', 'No-muerto'),
        ('6', 'Tauren'),
        ('7', 'Gnomo'),
        ('8', 'Troll'),
        ('9', 'Goblin'),
        ('10', 'Elfo de sangre'),
        ('11', 'Draenei'),
        ('12', 'Orco equivocado'),
        ('13', 'Continuar'),
        ('14', 'Roto'),
        ('15', 'Esqueleto'),
        ('16', 'Vrykul'),
        ('17', 'Tuskarr'),
        ('18', 'Trol del bosque'),
        ('19', 'Tono'),
        ('20', 'Esqueleto de Rasganorte'),
        ('21', 'Troll de hielo'),
        ('22', 'Huargen'),
        ('23', 'Gilnean'),
        ('24', 'Pandaren'),
        ('25', 'Pandaren'),
        ('26', 'Pandaren'),
        ('27', 'Nocheterna'),
        ('28', 'Tauren de montealto'),
        ('29', 'Elfo del vacío'),
        ('30', 'Draenei forjado por la luz'),
        ('31', 'Troll Zandalari'),
        ('32', 'Kul Tiran'),
        ('33', 'Humano'),
        ('34', 'Enano hierro negro'),
        ('35', 'Vulpera'),
        ('36', 'Orco Maghar'),
        ('37', 'Mecagnomo'),
    ]
    Playable_race = models.CharField(
        max_length=2, choices=p_race_choices, help_text="Introduce la raza del personaje")

    Level = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(120)], default=1, help_text="Introduce el nivel del personaje")

    Avatar_url = models.CharField(
        max_length=200, help_text="URL del Avatar", null=True
    )

    Bust_url = models.CharField(
        max_length=200, help_text="URL del Busto", null=True
    )

    Render_url = models.CharField(
        max_length=200, help_text="URL del Render", null=True
    )

    rank_choices = [
        ('7', 'Iniciado'),
        ('6', 'Alter'),
        ('5', 'Miembro'),
        ('4', 'Veternao'),
        ('3', 'Raider'),
        ('2', 'Alter Oficial'),
        ('1', 'Oficial'),
        ('0', 'GM'),
    ]
    Rank = models.CharField(
        max_length=1, choices=rank_choices, default=7, help_text="Introduce el rango del personaje")

    class Meta:
        ordering = ["Name"]

    def __str__(self):
        return self.Name


class Token(models.Model):
    """
    Clase que define la moneda
    """
    region_choices = [
        ('EU', 'EUROPA'),
        ('US', 'AMERICA')
    ]
    Region = models.CharField(
        max_length=2, choices=region_choices, primary_key=True, default='EU')
    Price = models.IntegerField(default=0)
    Last_update = models.DateTimeField()

    def __str__(self):
        return self.Region
