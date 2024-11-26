from api_requests import get_request
import datetime


# TODO не работает так как возращает html. Задал вопрос кирлесу
def get_meetings_calendar(start_date: str, end_date: str, departmentld: int, states: str):
    params = {
        'startDate': start_date,
        'endDate': end_date,
        'departmentld': departmentld,
        'states': states
        }
    url = 'https://test.vcc.uriit.ru/statistics/meetings-calendar'
    headers = {'accept: application/json': 'application/json'}
    return get_request(url=url, params=params, headers_1=headers)


# print(get_meetings_calendar(datetime.datetime.now() - datetime.timedelta(days=100), datetime.datetime.now(), 1, 'boo'))
