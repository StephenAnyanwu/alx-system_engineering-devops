#!/usr/bin/python3
"""
A python script that queries subscribers on a given Reddit API subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API for a given subreddit

    Parameters
    ----------
    subredddit : str
        Reddit API subreddit

    Returns
    -------
    int
        The number of subscribers (not active users, total subscribers).
        0 if an invalid subreddit is given.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        num_subscribers = data.get('data').get('subscribers')
        return num_subscribers
    else:
        return 0
