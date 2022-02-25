from django.core.management.base import BaseCommand
from app.models import Token
import json
import requests
from datetime import datetime


def blizzard_token():

    client_id = '2a3f57b9e9ca493b9caafdd338853adb'
    client_secret = 'aLb4rNxxs2snC8t77vC45gsumqh7yKdK'

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
            'https://eu.api.blizzard.com/data/wow/token/?namespace=dynamic-eu', headers=headers)

        response_format = response.content.decode('UTF-8')
        data = json.loads(response_format)

        coin = Token(
            Region='EU',
            Price=data["price"] / 10000,
            Last_update=datetime.now())
        coin.save()
