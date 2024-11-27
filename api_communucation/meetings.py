from api_communucation.api_requests import get_request, post_request, delete_request


def get_meetings(token: str, from_date_time, to_date_time):
    url = "http://test.vcc.uriit.ru/api/meetings"
    params = {
        "fromDatetime": from_date_time,
        "toDatetime": to_date_time
    }
    headers = {"Authorization": f"Bearer {token}"}
    return get_request(url=url, params=params, headers=headers)


def create_meetings(attachments: list[str], name: str, room_id: int, comment: str, participants_count: int,
                    send_notifications_at,
                    is_microphone_on: bool, is_video_on: bool, is_waiting_room_enabled: bool,
                    need_video_recording: bool, need_video_recording_2: bool,
                    external_url: str, permanent_room_id: int, started_at, ended_at, duration: int,
                    is_governo_presents: bool, is_notify_accepted: bool,
                    id_1: int, email: str, last_name: str, first_name: str, middle_name: str, id_2: int, frequency: int,
                    started_at_2, interval: int, count: int,
                    until, week_days: list[int], additional_dates: list, exclude_dates: list,
                    recurrence_update_type: str, is_virtual: bool, state: str,
                    backend: str, id_3: int, force: bool = None):
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
    params = {'force': force}
    headers = {'Content-Type': 'application/json'}
    return post_request(data=data, headers=headers, url=url, params=params)


def cancel_meeting(meeting_id: int, force: bool):
    params = {
        'meeting_id': meeting_id,
        'force': force
    }
    url = 'https://test.vcc.uriit.ru/api/meetings/'
    headers = {"Content-Type": 'application/json'}
    return delete_request(url=url, headers=headers, params=params)
