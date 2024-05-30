# utils/get_cpu_quota.py

import requests


def get_cpu_quota(username, token):
    response = requests.get(
        'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(
            username=username
        ),
        headers={'Authorization': 'Token {token}'.format(token=token)}
    )
    if response.status_code == 200:
        return response.content
    else:
        return 'Got unexpected status code {}: {!r}'.format(response.status_code, response.content)
