#!/usr/bin/python3
'''
     A script that queries the Reddit API for a given subreddit.
'''
import requests
from sys import argv


def top_ten(subreddit):
    '''Queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
    If subreddit is not valid, it prints None.
    '''
    user = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'
    response = requests.get(url, headers=user, allow_redirects=False)
    try:
        for post in response.json().get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)
