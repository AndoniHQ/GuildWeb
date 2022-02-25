from django.core.management.base import BaseCommand
from app.models import Character
import json
import requests


def blizzard_token():

    client_id = ''
    client_secret = ''

    data = {
        'grant_type': 'client_credentials'
    }

    response = requests.post('https://eu.battle.net/oauth/token',
                             data=data, auth=(client_id, client_secret))

    response_format = response.content.decode('UTF-8')
    data = json.loads(response_format)

    return data["access_token"]


class Command(BaseCommand):
    help = 'Test'

    def handle(self, *args, **options):
        headers = {
            'Authorization': 'Bearer ' + blizzard_token()
        }

        response = requests.get(
            'https://eu.api.blizzard.com/data/wow/guild/sanguino/saurfang-legacy/roster?namespace=profile-eu&locale=es_ES', headers=headers)

        if response.status_code == 200:

            Character.objects.all().delete()

            response_format = response.content.decode('UTF-8')
            data = json.loads(response_format)

            for i in range(0, len(data["members"])):
                player = Character(
                    Name=data["members"][i]["character"]["name"],
                    Realm=data["members"][i]["character"]["realm"]["slug"],
                    Playable_class=data["members"][i]["character"]["playable_class"]["id"],
                    Playable_race=data["members"][i]["character"]["playable_race"]["id"],
                    Level=data["members"][i]["character"]["level"],
                    Rank=data["members"][i]["rank"]
                )
                player.save()
        else:
            print("ERROR CODE:", response.status_code)
