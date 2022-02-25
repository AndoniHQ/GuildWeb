import json
import requests


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


# character_sync(client_id, client_secret)

def guild_sync():

    headers = {
        'Authorization': 'Bearer ' + blizzard_token()
    }

    response = requests.get(
        'https://eu.api.blizzard.com/data/wow/guild/sanguino/saurfang-legacy?namespace=profile-eu', headers=headers)

    response_format = response.content.decode('UTF-8')
    data = json.loads(response_format)

    print(data)


def token_sync():
    headers = {
        'Authorization': 'Bearer ' + blizzard_token()
    }

    response = requests.get(
        'https://eu.api.blizzard.com/data/wow/token/?namespace=dynamic-eu', headers=headers)

    response_format = response.content.decode('UTF-8')
    data = json.loads(response_format)
    print(data)


token_sync()
