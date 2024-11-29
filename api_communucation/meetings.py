import datetime

from api_communucation.api_requests import get_request, post_request, delete_request
from api_communucation.auth import login


def get_meetings(login_l, password_l, from_date_time, to_date_time, state=['booked', 'cancelled', 'started', 'ended'],
                 priority=None, name=None, department_id=None, user_id=False):
    '''передаешь все как и раньше, возращает теперь все как раньше, но таких словарей много и они лежат в списке,
    просто запусти for по возращаемым данным, остальное как раньше'''

    answer = []
    id = []
    page = 0
    flag = True
    url = "http://test.vcc.uriit.ru/api/meetings"
    print(1)
    responce_login = login(login_l, password_l)
    print(5)
    if responce_login[1] >= 300:
        print(2)
        raise Exception
    token = responce_login[0]['token']
    headers = {"Authorization": f"Bearer {token}"}
    while True:
        page += 1
        print('page', page)
        params = {
            "fromDatetime": from_date_time,
            "toDatetime": to_date_time,
            'userParticipant': responce_login[0]['user']['id'] if user_id else None,
            'state': state,
            'page': page,
            'priority': priority
            # 'departmentId': ''
        }
        if flag:
            responce = get_request(url=url, params=params, headers=headers)
            if responce[1] >= 300:
                print(responce[0])
                print(responce[1])
                raise Exception
            if not responce[0]['data']:
                return None
            for i in responce[0]['data']:
                if i['id'] not in id:
                    id.append(i['id'])
                    answer.append(i)
                else:
                    flag = False
                    break
        else:
            break
    return answer
"""    except Exception:
        return 'error'"""


# a = get_meetings('hantaton09', 'JK1zRww2N^3TWV2I', datetime.datetime(2024, 11, 20), datetime.datetime(2024, 11, 28),
#                 True)
# print(a)


def create_meetings(attachments: list[str] = [''], name: str = '', room_id: int = 0, comment: str = '',
                    participants_count: int = 0,
                    send_notifications_at=str(datetime.datetime.now()),
                    is_microphone_on: bool = False, is_video_on: bool = False, is_waiting_room_enabled: bool = False,
                    need_video_recording: bool = False, need_video_recording_2: bool = False,
                    external_url: str = '', permanent_room_id: int = 0, started_at=str(datetime.datetime.now()),
                    ended_at=str(datetime.datetime.now()), duration: int = 0,
                    is_governo_presents: bool = False, is_notify_accepted: bool = False,
                    id_1: int = 0, id_2: int = 0, frequency: int = 0,
                    started_at_2=str(datetime.datetime.now()), interval: int = 0, count: int = 0,
                    until=str(datetime.datetime.now()), week_days: list[int] = [0], additional_dates: list = [],
                    exclude_dates: list = [], recurrence_update_type: str = '', is_virtual: bool = False,
                    state: str = '', backend: str = '', id_3: int = 0, token: str = '', force: bool = None,
                    email: str = 'н/д', last_name: str = 'н/д', first_name: str = 'н/д', middle_name: str = 'н/д'):
    print(duration)
    url = 'https://test.vcc.uriit.ru/api/meetings'
    data = {
        "attachments": attachments,
        "name": name,
        "roomId": room_id,
        "comment": comment,
        "participantsCount": participants_count,
        "sendNotificationsAt": send_notifications_at,  # datetime.datetime
        "ciscoSettings": {
            "isMicrophoneOn": is_microphone_on,
            "isVideoOn": is_video_on,
            "isWaitingRoomEnabled": is_waiting_room_enabled,
            "needVideoRecording": need_video_recording
        },
        "vinteoSettings": {
            "needVideoRecording": need_video_recording_2
        },
        "externalSettings": {
            "externalUrl": external_url,
            "permanentRoomId": permanent_room_id
        },
        "startedAt": started_at,  # datetime.datetime
        "endedAt": ended_at,  # datetime.datetime
        "duration": duration,
        "isGovernorPresents": is_governo_presents,
        "isNotifyAccepted": is_notify_accepted,
        "participants": [
            {
                "id": id_1
            },
            {
                "email": email,
                "lastName": last_name,
                "firstName": first_name,
                "middleName": middle_name
            }
        ],
        "groups": [
            {
                "id": id_2
            }
        ],
        "recurrence": {
            "frequency": frequency,
            "startedAt": started_at_2,  # datetime.datetime
            "interval": interval,
            "count": count,
            "until": until,  # datetime.datetime
            "weekDays": week_days,
            "additionalDates": additional_dates,  # list[datetime.datetime]
            "excludeDates": exclude_dates  # list[datetime.datetime]
        },
        "recurrenceUpdateType": recurrence_update_type,
        "isVirtual": is_virtual,
        "state": state,
        "backend": backend,
        "organizedBy": {
            "id": id_3
        }
    }
    print(duration)
    hh = {
        "name": name,
        "ciscoSettings": {
            "isMicrophoneOn": is_microphone_on,
            "isVideoOn": is_video_on,
            "isWaitingRoomEnabled": is_waiting_room_enabled
        },
        "participantsCount": participants_count,
        "startedAt": "2024-11-08T12:00:00",
        "duration": duration,
        "participants": [],
        "sendNotificationsAt": "2024-11-08T11:45:00",
        "state": "booked"
    }

    params = {'force': True}
    print(duration)
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'}

    a = post_request(data=hh, headers=headers, url=url, params=params)
    return a


'''
create_meetings(name="test_dpp", is_microphone_on=bool('True'), is_video_on=bool('True'),
                is_waiting_room_enabled=bool('True'),
                participants_count=int('5'), started_at=str(datetime.datetime(2024, 11, 8, 12, 00, 00)), duration=int('120'),
                id_1=int('5'), send_notifications_at=str(datetime.datetime(2024, 11, 8, 11, 45, 00)), state='booked', token=login("hantaton09", "JK1zRww2N^3TWV2I")[0]['token'])
'''


def cancel_meeting(login_l, password_l, meeting_id: int, force: bool):
    params = {
        'meeting_id': meeting_id,
        'force': force
    }
    url = 'https://test.vcc.uriit.ru/api/meetings/'
    token = login(login_l=login_l, password_l=password_l)[0]['token']
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'}
    return delete_request(url=url, headers=headers, params=params)


def get_meeting(login_l, password_l, meeting_id=''):
    print(login_l, password_l, meeting_id)
    token = login(login=login_l, password=password_l)[0]['token']
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'}
    url = 'https://test.vcc.uriit.ru/api/meetings/' + str(meeting_id)
    return get_request(url=url, headers=headers)


print(get_meeting('hantaton09', 'JK1zRww2N^3TWV2I', 1391))
