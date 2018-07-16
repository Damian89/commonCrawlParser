#!/usr/bin/env python
# coding: utf8

import sys

import queue

if sys.version_info < (3, 0):
    sys.stdout.write("Sorry, Python 3.x is required\n")
    sys.exit(1)

from inc.arguments import getArguments
from inc.write import writeResults
from inc.index import filterIndices, getIndices
from inc.extract import extractLinksFromCC
from inc.worker import WorkerThread
from inc.request import makeCCUrl

def main():
    ccEntries = []
    threads = []

    domain, outfile, max_threads, filterWords = getArguments()

    indices = getIndices()
    indices = filterIndices(filterWords, indices)

    queueAll = queue.Queue()

    for i in range(0, max_threads):
        print("\033[32m[ i ]\033[0m Worker {} started...".format(i))
        worker = WorkerThread(queueAll, i, ccEntries)
        worker.setDaemon(True)
        worker.start()
        threads.append(worker)

    for index in indices:
        queueAll.put([index, makeCCUrl(domain, index)])

    for item in threads:
        item.join()

    print("\033[32m[ i ]\033[0m Finished all requests")

    print("\033[32m[ i ]\033[0m Extracting links...")
    links = extractLinksFromCC(ccEntries)
    print("\033[32m[ i ]\033[0m Found {} lines in responses".format(len(links)))

    print("\033[32m[ i ]\033[0m Writing links to {}".format(outfile))
    writeResults(links, outfile)

    print("\033[32m[ i ]\033[0m Finished!")


if __name__ == "__main__":
    main()
