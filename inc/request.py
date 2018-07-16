#!/usr/bin/env python
# coding: utf8

import requests


def getCCResponse(url):
    try:
        response = requests.get(url, headers={
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'accept-language': 'en-US,en;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'referer': url,
        }, verify=False, timeout=10, allow_redirects=True)

        if response.status_code != 200:
            print("\033[31m[ ! ]\033[0m Statuscode not 200 ... resuming but this is not normal...")

    except Exception as e:
        print("\033[31m[ ! ]\033[0m Exception ... resuming but this is not normal...")
        print(e)

    return response.text.split("\n")[:-1]


def makeCCUrl(domain, index):
    url = "https://index.commoncrawl.org/" + index + "-index?url=*." + domain + "&output=json".format()
    return url
