from api_communucation.api_requests import get_request, post_request, delete_request


def get_meetings(token: str, from_date_time, to_date_time):
    url = "http://test.vcc.uriit.ru/api/meetings"
    params = {
        "fromDatetime": from_date_time,
        "toDatetime": to_date_time
    }
    headers = {"Authorization": f"Bearer {token}"}
    return get_request(url=url, params=params, headers=headers)


token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjp7ImlkIjo1NTIsImRlcGFydG1lbnRfaWQiOjIsInBvc3QiOm51bGwsInBlcm1pc3Npb25zIjpbImdyb3VwLmxpc3QiLCJ1c2VyLmxpc3QiLCJncm91cC5kZWxldGUiLCJ1c2VyLmNyZWF0ZV9wdWJsaWMiLCJidWlsZGluZy5saXN0IiwidXNlci51cGRhdGVfcHVibGljIiwibWVldGluZy5kZWxldGUiLCJwZXJtYW5lbnRfcm9vbS5saXN0IiwiZmlsZS5jcmVhdGUiLCJtZWV0aW5nLnVwZGF0ZSIsImdyb3VwLnVwZGF0ZSIsInJvb20ubGlzdCIsIm11bmljaXBhbF9hcmVhLmxpc3QiLCJzZXR0aW5nLmxpc3QiLCJtZWV0aW5nLmxpc3QiLCJyb2xlLnBlcm1pc3Npb25zX2xpc3QiLCJlbWFpbF90ZW1wbGF0ZXMubGlzdCIsImZpbGUubGlzdCIsIm1lZXRpbmcuY3JlYXRlIiwiZXZlbnQubGlzdCIsInN0YXRpc3RpY3MubGlzdCIsImRlcGFydG1lbnQubGlzdCIsImdyb3VwLmNyZWF0ZSIsInJvbGUubGlzdCJdLCJsb2dpbiI6ImhhbnRhdG9uMDkiLCJlbWFpbCI6ImhhbnRhdG9uMDkuaEBtYWlsLnJ1IiwibGFzdF9uYW1lIjoiXHUwNDI1XHUwNDMwXHUwNDNkXHUwNDQyXHUwNDMwXHUwNDQyXHUwNDNlXHUwNDNkXHUwNDNlXHUwNDMyIiwiZmlyc3RfbmFtZSI6Ilx1MDQyNVx1MDQzMFx1MDQzZFx1MDQ0Mlx1MDQzMFx1MDQ0Mlx1MDQzZVx1MDQzZCIsIm1pZGRsZV9uYW1lIjoiIiwiYmlydGhkYXkiOm51bGwsInBob25lIjpudWxsLCJ1cGRhdGVkX2F0IjoxNzMyMjg4MjIyLjAsInByaW9yaXR5IjoyLCJyb2xlcyI6W3sibmFtZSI6Ilx1MDQxZVx1MDQ0MFx1MDQzM1x1MDQzMFx1MDQzZFx1MDQzOFx1MDQzN1x1MDQzMFx1MDQ0Mlx1MDQzZVx1MDQ0MCIsImRlc2NyaXB0aW9uIjoiXHUwNDFlXHUwNDQwXHUwNDMzXHUwNDMwXHUwNDNkXHUwNDM4XHUwNDM3XHUwNDMwXHUwNDQyXHUwNDNlXHUwNDQwIFx1MDQzMlx1MDQzOFx1MDQzNFx1MDQzNVx1MDQzZVx1MDQzYVx1MDQzZVx1MDQzZFx1MDQ0NFx1MDQzNVx1MDQ0MFx1MDQzNVx1MDQzZFx1MDQ0Nlx1MDQzOFx1MDQzOSIsImlkIjozLCJwZXJtaXNzaW9ucyI6WyJidWlsZGluZy5saXN0IiwiZGVwYXJ0bWVudC5saXN0IiwiZW1haWxfdGVtcGxhdGVzLmxpc3QiLCJldmVudC5saXN0IiwiZmlsZS5saXN0IiwibWVldGluZy5jcmVhdGUiLCJtZWV0aW5nLmRlbGV0ZSIsIm1lZXRpbmcubGlzdCIsIm1lZXRpbmcudXBkYXRlIiwibXVuaWNpcGFsX2FyZWEubGlzdCIsInJvbGUubGlzdCIsInJvbGUucGVybWlzc2lvbnNfbGlzdCIsInJvb20ubGlzdCIsInNldHRpbmcubGlzdCIsInVzZXIubGlzdCIsInN0YXRpc3RpY3MubGlzdCIsImZpbGUuY3JlYXRlIiwicGVybWFuZW50X3Jvb20ubGlzdCIsImdyb3VwLmxpc3QiLCJncm91cC5jcmVhdGUiLCJncm91cC51cGRhdGUiLCJncm91cC5kZWxldGUiLCJwZXJtYW5lbnRfcm9vbS5saXN0IiwidXNlci5jcmVhdGVfcHVibGljIiwidXNlci51cGRhdGVfcHVibGljIl19XX0sInRva2VuX2V4cGlyZWRfYXQiOjE3MzI3MTMwODguMCwidG9rZW5fY3JlYXRlZF9hdCI6MTczMjY5ODY4OC4wLCJyZWZyZXNoX3Rva2VuIjoiZXlKMGVYQWlPaUpLVjFRaUxDSmhiR2NpT2lKSVV6STFOaUo5LmV5SjFjMlZ5WDJsa0lqbzFOVElzSW1WNGNDSTZNVGN6TXpNd016UTRPQzR3TENKMWNHUWlPakUzTXpJeU9EZ3lNakl1TUN3aWRIbHdJam9pY21WbWNtVnphQ0o5LjRqeUJlS1owTTFrSnM0ODVKMjRmcXlRb2h4bXBfd1JGeGhpYWVVMU1lLWcifQ.Rkvm4ALaGoLH4t0FPnFzVjSBie-xwar3ekgIZQFqeJA"


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


# TODO тоже самое сайт хуйня кирлессу написал
def cancel_meeting(meeting_id: int, force: bool):
    params = {
        'meeting_id': meeting_id,
        'force': force
    }
    url = 'https://test.vcc.uriit.ru/api/meetings/'
    headers = {"Content-Type": 'application/json'}
    return delete_request(url=url, headers=headers, params=params)
