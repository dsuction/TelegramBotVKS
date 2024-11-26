import requests
import json
import requests


def auth_login(login: str, password: str):
    data = {
        "login": login,
        "password": password,
        "fingerprint": {}
    }
    headers = {"Content-Type": "application/json"}

    response = requests.post('https://test.vcc.uriit.ru/api/auth/login', data=json.dumps(data), headers=headers)

    return response.json()

