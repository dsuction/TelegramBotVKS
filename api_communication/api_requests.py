import requests
import json


def get_request(url: str, params, headers_1):
    response = requests.get(url=url, params=params, headers=headers_1)
    return response.text, response.status_code


def post_request(data: dict, headers: dict, url: str, params: dict=None):
    response = requests.post(url=url, data=json.dumps(data), headers=headers, params=params)
    return response.json(), response.status_code


def delete_request(url: str, params: dict, headers: dict):
    response = requests.delete(url=url, params=params, headers=headers)
    return response, response.status_code


def put_request():
    pass
