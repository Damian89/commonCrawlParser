#!/usr/bin/env python
# coding: utf8

import requests


def getCCResponse(url):
    try:
        response = requests.get(url, verify=False, timeout=10, allow_redirects=True)

        if response.status_code != 200:
            print("\033[31m[!!]\033[0m Statuscode not 200 ... resuming but this is not normal...")

    except Exception as e:
        print("\033[31m[!!]\033[0m Exception ... resuming but this is not normal...")
        print(e)

    return response.text.split("\n")[:-1]


def makeCCUrl(domain, index):
    url = "http://index.commoncrawl.org/" + index + "-index?url=*." + domain + "&output=json".format()
    return url
