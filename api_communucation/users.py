from api_communucation.api_requests import post_request


def create_user(login: str = '', password: str = '', email: str = '', last_name: str = '', first_name: str = '', middle_name: str = '', phone: str = '', birthday: str = '', role_ids: list[int] = '', priority: int = '', departament_id: int = '', is_send_email: bool = ''):
    data = {
            "login_L": login,
            "password": password,
            "email": email,
            "lastName": last_name,
            "firstName": first_name,
            "middleName": middle_name,
            "phone": phone,
            "birthday": birthday,
            "roleIds": role_ids[:],
            "priority": priority,
            "departmentId": departament_id,
            "isSendEmail": is_send_email
    }

    headers = {'Content-Type': 'application/json'}

    url = 'https://test.vcc.uriit.ru/api/users'

    return post_request(data=data, headers=headers, url=url)

    
print(create_user('string', 'string', 'user@example.com', 'string', 'string', 'string', 'string', '2024-11-26', [5], 3, 1, True))
