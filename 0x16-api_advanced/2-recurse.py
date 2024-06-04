#!/usr/bin/python3
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """Recursively retrieves titles of all hot articles for given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python:reddit_scraper:v1.0 (by /u/Emording)"}
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data")
        after = data.get("after")
        count += data.get("dist")

        for child in data.get("children"):
            hot_list.append(child.get("data").get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after, count)

        return hot_list

    elif response.status_code == 404:
        return None

    else:
        return None
