from api_communucation.api_requests import get_request


def get_meetings(token, from_date_time, to_date_time):
    url = "http://test.vcc.uriit.ru/api/meetings"
    params = {
                    "fromDatetime": from_date_time,
                    "toDatetime": to_date_time
                   }
    headers = {"Authorization": f"Bearer {token}"}
    return get_request(url=url, params=params, headers=headers)
