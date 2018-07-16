#!/usr/bin/env python
# coding: utf8

import json
import sys


def extractLinksFromCC(ccEntries):
    links = []

    for entry in ccEntries:
        for link in entry:
            try:

                link = json.loads(link)["url"]
                link = link.strip()
                links.append(link + "\n")

            except ValueError as e:
                # This is caused when the server fails and we dont have a valid json response
                pass

    if len(links) == 0:
        print("\033[31m[ ! ]\033[0m No links found... sorry!")
        sys.exit()

    return list(set(links))
