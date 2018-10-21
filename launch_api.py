from datetime import datetime

import requests

API_URL = "https://launchlibrary.net/1.4/"


def get_all_launches():
    response = pass_request("launch/1960-01-01/" + datetime.now().strftime("%Y-%m-%d") + "?limit=2000")
    return response['launches']


def pass_request(subpath):
    return requests.get(url=API_URL + subpath).json()
