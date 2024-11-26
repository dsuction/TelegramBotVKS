from api_requests import post_request


# login_test = "hantaton09"
# password_test = "JK1zRww2N^3TWV2I"


def login(login: str, password: str): 
    data = {
    "login": login,
    "password": password,
    "fingerprint": {}
    }

    headers = {"Content-Type": "application/json"}

    url = 'https://test.vcc.uriit.ru/api/auth/login'

    return post_request(data=data, headers=headers,  url=url)



def register():
    pass


def logout():
    pass
# 
# 
# def refresh_token(token):
#     data = {"token": ""}
#     
#     headers = {"Content-Type": "application/json"}
#  
#     response = requests.post('https://test.vcc.uriit.ru/api/auth/refresh-token', data=json.dumps(data), headers=headers)
# 
#     return response.json(), response.status_code
# 
# print(refresh_token(login(login_test, password_test)[0]['token']))
# 
# 
def reset_password():
    pass


def reset_password_confirm():
    pass


def ldap_login():
    pass
