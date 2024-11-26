def create_user(login: str, password: str, email: str, last_name: str, first_name: str, middle_name: str, phone: str, birthday: str, role_ids: list[int], priority: int, departament_id: int, is_send_email: bool):
    data = {
            "login": login,
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

    

create_user()