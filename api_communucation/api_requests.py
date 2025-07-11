import requests
import json


def get_request(url: str, headers, params={}):
    response = requests.get(url=url, params=params, headers=headers)
    return response.json(), response.status_code


def post_request(data: dict, headers: dict, url: str, params=None):
    response = requests.post(url=url, data=json.dumps(data), headers=headers, params=params)
    return response.json(), response.status_code


def delete_request():
    pass
