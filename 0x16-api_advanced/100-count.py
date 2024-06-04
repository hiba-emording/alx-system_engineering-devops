#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit"""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """Function to count words in all hot posts of a given Reddit subreddit"""
    if not word_list or not subreddit:
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "/u/Emording)"}
    params = {"limit": 100}

    if after:
        params["after"] = after

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data")
        children = data.get("children", [])

        for post in children:
            title = post.get("data", {}).get("title", "").lower()
            for word in word_list:
                if word.lower() in title:
                    counts[word.lower()] = counts.get(word.lower(), 0)
                    + title.count(word.lower())

        after = data.get("after")

        if after:
            count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print("{}: {}".format(word.lower(), count))
