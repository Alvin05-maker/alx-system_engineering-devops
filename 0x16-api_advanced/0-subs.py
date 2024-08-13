#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers
for a given subreddit"""

import json
import requests


def get_access_token():
    """get access token for reddit api"""
    client_auth = requests.auth.HTTPBasicAuth(
        'nvpEVDdQS4zT14w1GbeijA', '7NnqmfNOdfnj1fgOqDTLYrRFCFZ2jw')
    response = requests.post(url='https://www.reddit.com/api/v1/access_token',
                             data={
                                 'username': 'Voidox1',
                                 'password': 'Smart@reddit1',
                                 'grant_type': 'password'
                             },
                             headers={
                                 'User-Agent': 'my-app/0.0.1 by void1x2x11'},
                             auth=client_auth
                             )
    return response.json().get('access_token', None)


def number_of_subscribers(subreddit):
    """return number of subscribers for a subreddit"""

    headers = {
        'User-Agent': 'my-app/0.0.1 by void1x2x11',
        'Authorization': f'Bearer {get_access_token()}'
    }
    url = f"https://oauth.reddit.com/r/{subreddit}/about/"

    response = requests.get(url, headers=headers)
    subscribers = int(response.json()['data']['subscribers']) \
        if response.status_code == 200 else 0

    return subscribers
