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
        success_sync = 0

        for pj in Character.objects.all():

            response = requests.get(
                "https://eu.api.blizzard.com/profile/wow/character/" + pj.Realm.lower() + "/" + pj.Name.lower() + "/character-media?namespace=profile-eu&locale=es_ES", headers=headers)

            if response.status_code == 200:

                response_format = response.content.decode('UTF-8')
                data = json.loads(response_format)

                Character.objects.filter(Name=pj.Name).update(
                    Avatar_url=data["avatar_url"])
                Character.objects.filter(Name=pj.Name).update(
                    Bust_url=data["bust_url"])
                Character.objects.filter(Name=pj.Name).update(
                    Render_url=data["render_url"])

                success_sync += 1

            print(response, pj.Name)

        Success_rate = str(success_sync) + "/" + \
            str(Character.objects.all().count())
        Success_percentage = success_sync/Character.objects.all().count()*100
        print("Media links obtained for", Success_rate, "Success rate:", Success_percentage,"%")
