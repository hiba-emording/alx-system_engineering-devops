#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts for a given subreddit"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "u/Emording"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        results = response.json().get("data")
        [print(k.get("data").get("title")) for k in results.get("children")]
    else:
        print("None")
