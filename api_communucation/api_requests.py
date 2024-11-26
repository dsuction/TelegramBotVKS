import requests
import json


def get_request(url: str, params, headers):
    response = requests.get(url=url, params=params, headers=headers)
    return response.json(), response.status_code


def post_request(data: dict, headers: dict, url: str):
    response = requests.post(url=url, data=json.dumps(data), headers=headers)
    return response.json(), response.status_code


def delete_request():
    pass


def put_request():
    pass
