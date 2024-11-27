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
             middle_name: str = 'Родионович', phone: str = '', birthday: str = '2007-11-05', role_id: int = 5,
             type_s: str = 'native'):
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

"""
print(register(login='denisa', password='printMail', email='da0434395@gmail.com', last_name='андреев',
               first_name='денис', middle_name='андреевич', phone='79658338148', birthday='2007-10-08', role_id=5,
               type_s='native'))"""


def logout():
    pass

def reset_password():
    pass


def reset_password_confirm():
    pass


def ldap_login():
    pass
