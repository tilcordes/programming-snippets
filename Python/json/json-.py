import json
import requests

def local_json():
    with open('bitcoin.json') as file:
        data = json.load(file)

    print(data)
    print(data['bpi']['EUR']['rate_float'])

    data['bpi']['EUR']['rate_float'] = 555

    print(data)
    print(data['bpi']['EUR']['rate_float'])

def json_api():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    request = requests.get(url=url)
    data = request.json()
    print(data)