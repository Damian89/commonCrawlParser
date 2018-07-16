#!/usr/bin/env python
# coding: utf8

import threading
from inc.request import getCCResponse


stopSet = True

class WorkerThread(threading.Thread):
    def __init__(self, queue, tid, ccEntries):
        threading.Thread.__init__(self)
        self.queue = queue
        self.tid = tid
        self.ccEntries = ccEntries

    def run(self):
        global stopSet

        while stopSet:

            # Check if items in queue
            try:
                index, url = self.queue.get(timeout=1)
            except Exception as e:
                stopSet = False
                break

            try:
                print("\033[32m[ i ]\033[0m Request to {}".format(index))

                lines = getCCResponse(url)
                self.ccEntries.append(lines)

            except Exception as e:
                # Just in case we have a valid exception, because requests failed not by Timeout or MaxRetries,
                # force thread to stop... you will have to check this error out...

                print(
                    "Unknown exception caught... to prevent infinite loops, thread has to stop..."
                )
                break

            self.queue.task_done()