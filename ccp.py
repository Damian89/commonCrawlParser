#!/usr/bin/env python
# coding: utf8

import sys

if sys.version_info < (3, 0):
    sys.stdout.write("Sorry, Python 3.x is required\n")
    sys.exit(1)


from inc.request import getCCResponse,makeCCUrl
from inc.arguments import getArguments
from inc.write import writeResults
from inc.index import filterIndices, getIndices, intersectLists
from inc.extract import extractLinksFromCC

def main():
    domain, outfile, index_used = getArguments()

    indices = getIndices()
    indices = filterIndices(index_used, indices)

    ccEntries = []

    for index in indices:
        print("\033[32m[ i ]\033[0m Request to {}".format(index))

        url = makeCCUrl(domain, index)
        lines = getCCResponse(url)
        ccEntries.append(lines)

    print("\033[32m[ i ] Finished all requests \033[0m")

    print("Extracting links...")
    links = extractLinksFromCC(ccEntries)
    print("Found {} lines in responses".format(len(links)))

    print("Writing links to {}".format(outfile))
    writeResults(links, outfile)

    print("Finished!")

if __name__ == "__main__":
    main()