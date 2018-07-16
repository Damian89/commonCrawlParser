#!/usr/bin/env python
# coding: utf8

import os
import json
import sys


def getIndices():
    work_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    indices_path = os.path.join(work_path, "data", "indices.json")
    with open(indices_path) as f:
        data = json.load(f)
    indexlist = []
    for element in data:
        indexlist.append(element["index"])

    return indexlist


def filterIndices(filterWords, indices):
    if filterWords is None:
        return indices

    newIndices = []

    for index in indices:
        for word in filterWords:
            if word in index:
                newIndices.append(index)

    if len(newIndices) == 0:
        print("\033[31m[ ! ] Not indices selected, may your filter is wrong!\033[0m")
        sys.exit()

    return newIndices


def intersectLists(indices, index_used_list):
    lst3 = [value for value in indices if value in index_used_list]
    return lst3
