#!/usr/bin/python3
"""queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddi"""

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


def top_ten(subreddit):
    """return top 10 post on subreddit"""
    headers = {
        'Authorization': f'Bearer {get_access_token()}',
        'User-Agent': 'my-app/0.0.1 by void1x2x11'
    }

    url = f"https://oauth.reddit.com/r/{subreddit}/hot/?limit=9"
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return (print(None))

    top_ten = response.json().get('data', {}).get("children", [])
    for post in top_ten:
        print(post.get('data').get('title'))
