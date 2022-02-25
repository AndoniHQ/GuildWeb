import requests
import json


def extract_values(obj, key):
    """Pull all values of specified key from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results


client_id = '2a3f57b9e9ca493b9caafdd338853adb'
client_secret = 'aLb4rNxxs2snC8t77vC45gsumqh7yKdK'

data = {
    'grant_type': 'client_credentials'
}

response = requests.post('https://eu.battle.net/oauth/token',
                         data=data, auth=(client_id, client_secret))

response_format = response.content.decode('UTF-8')
data = json.loads(response_format)

print("Getting token")
print(data["access_token"])

headers = {
    'Authorization': 'Bearer ' + data["access_token"]
}

response = requests.get(
    'https://eu.api.blizzard.com/data/wow/guild/sanguino/saurfang-legacy/roster?namespace=profile-eu&locale=es_ES', headers=headers)

response_format = response.content.decode('UTF-8')
data = json.loads(response_format)

print("Getting query")

u = 0
for i in range(0, len(data["members"])):
    print(data["members"][i]["character"]["name"])
    print(data["members"][i]["character"]["realm"]["slug"])
    print(data["members"][i]["character"]["level"])
    print(data["members"][i]["character"]["playable_class"]["id"])
    print(data["members"][i]["character"]["playable_race"]["id"])
    print(data["members"][i]["rank"])
    u += 1

print(u)


# print(len(data["members"]))
