import requests
import json

URL = 'https://gql.twitch.tv/gql'
headers = {'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko'}
data = [{
    "operationName": "ChatViewers",
    "variables": {
        "channelLogin": "monkeymagic0007"
    },
    "extensions": {
        "persistedQuery": {
            "version": 1,
            "sha256Hash": "e0761ef5444ee3acccee5cfc5b834cbfd7dc220133aa5fbefe1b66120f506250"
        }
    }
}]


response = requests.post(URL, headers=headers, data=json.dumps(data))

chatters = response.json().pop()['data']['channel']['chatters']

keys = ['staff', 'moderators', 'vips', 'viewers']

user_list = []

for key in keys:
    for chatter_data in chatters[key]:
        user_list.append(chatter_data['login'])

print(user_list)
