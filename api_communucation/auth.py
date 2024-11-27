from api_communucation.api_requests import post_request


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


def register(login: str = '', password: str = '', email: str = '', last_name: str = '', first_name: str = '',
             middle_name: str = '', phone: str = '', birthday: str = '', role_id: int = 5,
             type_s: str = ''):
    data = {
        "login": login,
        "password": password,
        "email": email,
        "lastName": last_name,
        "firstName": first_name,
        "middleName": middle_name,
        "phone": phone,
        "birthday": birthday,
        "roleId": role_id,
        "type": type_s
    }
    headers = {'Content-Type': 'application/json'}
    url = 'https://test.vcc.uriit.ru/api/auth/register'
    return post_request(data=data, headers=headers, url=url)


def logout():
    pass


def reset_password():
    pass


def reset_password_confirm():
    pass


def ldap_login():
    pass
