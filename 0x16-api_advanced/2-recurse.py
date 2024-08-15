#!/usr/bin/python3
"""
Recursively queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
If the subreddit is invalid or no results are found, it returns None.
"""

import requests


def recurse(subrddit, hot_list=[], after=None):
    u = f'https://www.reddit.com/r/{subrddit}/hot.json?limit=100&after={after}'

    if after is None:
        url = f'https://www.reddit.com/r/{subrddit}/hot.json?limit=100'
    else:
        url = u

    headers = {'User-Agent': 'by u/x'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            hot_list.append(post['data']['title'])

        after = data['data']['after']
        if after is not None:
            return recurse(subrddit, hot_list, after)
        else:
            return hot_list
    else:
        return None


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subrddit = sys.argv[1]
        result = recurse(subrddit)
        if result is not None:
            print(len(result))
        else:
            print("None")
