from api_communucation.api_requests import post_request, get_request
from api_communucation.auth import login


def update_user_info(login_l, password, password_new='', firs_name_new='', last_name_new='', middle_name_new='',
                     email_new='', phone_new='', birthday_new=''):
    """
    Отправь сюда только аргументы, которые хочешь изменить в аккаунте, все остальные останутся прежними, первые два
    аргумента: логин и пароль обязательные!
    """

    responce = login(login_l, password)

    if responce[1] < 300:
        data = {
            "password": password_new if password_new else password,
            "firstName": firs_name_new if firs_name_new else responce[0]['user']['firstName'],
            "lastName": last_name_new if last_name_new else responce[0]['user']['lastName'],
            "middleName": middle_name_new if middle_name_new else responce[0]['user']['middleName'],
            "email": email_new if email_new else responce[0]['user']['email'],
            "phone": phone_new if phone_new else responce[0]['user']['phone'],
            "birthday": birthday_new if birthday_new else responce[0]['user']['birthday']
        }
        headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {responce[0]["token"]}'}
        url = 'https://test.vcc.uriit.ru/api/account/user-info'
        return post_request(data=data, headers=headers, url=url)[0]
    return 'error'


def get_user_info(login_l, password):
    responce = login(login_l, password)
    print(responce)
    if responce[1] < 300:
        headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {responce[0]["token"]}'}
        url = 'https://test.vcc.uriit.ru/api/account/user-info'
        return get_request(url=url, headers=headers)[0]
    return 'error'


# print(get_user_info('hantaton09', 'Хантатататон'))
