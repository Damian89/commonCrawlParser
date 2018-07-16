#!/usr/bin/env python
# coding: utf8

def writeResults(links, outfile):
    fw = open(outfile, "w")
    for link in links:
        fw.write(link)
