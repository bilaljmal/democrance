import time

import requests
import json
from django.conf import settings

from .models import RoleGroup

base = settings.OIDC_HOST
realm = settings.OIDC_REALM


def create_user(token, **data):
    url = f"{base}/admin/realms/{realm}/users"
    payload = json.dumps({
        "username": data["username"],
        "email": data["email"],
        "firstName": data["first_name"],
        "lastName": data["last_name"],
        "enabled": True,
        "emailVerified": False,
        "credentials": [
            {
                "type": "password",
                "value": data["password"],
                "temporary": False
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + str(token)
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    user_id = get_user_id(token, data["username"])
    user_code = user_id.json()[0]['id']
    default = RoleGroup.objects.filter(group_name="signup").first().group_code
    assigned = RoleGroup.objects.filter(id=data["user_roles"].id).first().group_code
    add_user_to_group(token, user_code, assigned)
    remove_user_from_group(token, user_code, default)

    # print(res)
    return response, user_code


def update_user(token, userid, **data):
    url = f"{base}/admin/realms/{realm}/users/{userid}"
    payload = json.dumps({
        "email": data["email"],
        "firstName": data["first_name"],
        "lastName": data["last_name"],
        "enabled": True,
        "emailVerified": True,
        "attributes": {
            "display_picture": data["display_picture"] if "display_picture" in data else ""
        }

    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + str(token)
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    return response


def deactivate_user(token, userid, status):
    url = f"{base}/admin/realms/{realm}/users/{userid}"
    payload = json.dumps({
        "enabled": status,
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + str(token)
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    return response


def reset_password_user(token, userid, **data):
    url = f"{base}/admin/realms/{realm}/users/{userid}"
    payload = json.dumps({
        "credentials": [
            {
                "type": "password",
                "value": data["password"],
                "temporary": False
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + str(token)
    }
    response = requests.request("PUT", url, headers=headers, data=payload)

    return response


def get_user_id(token, username):
    url = f"{base}/admin/realms/{realm}/users?username={username}"

    payload = json.dumps({})
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + str(token)
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response


def add_user_to_group(token, user_id, group_id):
    url = f"{base}/admin/realms/{realm}/users/{user_id}/groups/{group_id}"
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.put(url.strip(), headers=headers)
    print(response.status_code)
    return response


def remove_user_from_group(token, user_id, group_id):
    url = f"{base}/admin/realms/{realm}/users/{user_id}/groups/{group_id}"
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.delete(url, headers=headers)
    return response


def update_role(token, userid, default, assign):
    remove_user_from_group(token, userid, default)
    add_user_to_group(token, userid, assign)


def update_role_self(token, userid):
    user_id=get_user_id(token,userid).json()[0]['id']
    assigned = RoleGroup.objects.filter(group_name="owner").first()
    add_user_to_group(token, user_id, assigned.group_code)
    return user_id,assigned
