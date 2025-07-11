from api_requests import get_request
import datetime


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
