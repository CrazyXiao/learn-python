################################################################################
# util/thread_helper.py
#
# Created by Greg Bayer <greg@gbayer.com>.
# Open sourced at http://github.com/gregbayer/python-threading-utils
################################################################################

import threading
import logging
import sys
import queue

def do_threaded_work(work_items, work_func, num_threads=None, per_sync_timeout=1, preserve_result_ordering=True):
    """ Executes work_func on each work_item. Note: Execution order is not preserved, but output ordering is (optionally).

        Parameters:
        - num_threads               Default: len(work_items)  --- Number of threads to use process items in work_items.
        - per_sync_timeout          Default: 1                --- Each synchronized operation can optionally timeout.
        - preserve_result_ordering  Default: True             --- Reorders result_item to match original work_items ordering.

        Return:
        --- list of results from applying work_func to each work_item. Order is optionally preserved.

        Example:

        def process_url(url):
            # TODO: Do some work with the url
            return url

        urls_to_process = ["http://url1.com", "http://url2.com", "http://site1.com", "http://site2.com"]
        # process urls in parallel
        result_items = do_threaded_work(urls_to_process, process_url)

        # print results
        print repr(result_items)
    """
    if not num_threads:
        num_threads = len(work_items)

    work_queue = queue.Queue()
    result_queue = queue.Queue()

    index = 0
    for work_item in work_items:
        if preserve_result_ordering:
            work_queue.put((index, work_item))
        else:
            work_queue.put(work_item)
        index += 1

    if preserve_result_ordering:
        wrapped_work_func = lambda work_item: (work_item[0], work_func(work_item[1]))

    start_logging_with_thread_info()

    # spawn a pool of threads, and pass them queue instance
    for _ in range(num_threads):
        if preserve_result_ordering:
            t = ThreadedWorker(work_queue, result_queue, work_func=wrapped_work_func, queue_timeout=per_sync_timeout)
        else:
            t = ThreadedWorker(work_queue, result_queue, work_func=work_func, queue_timeout=per_sync_timeout)
        t.setDaemon(True)
        t.start()

    work_queue.join()
    stop_logging_with_thread_info()

    logging.info('work_queue joined')

    result_items = []
    while not result_queue.empty():
        result = result_queue.get(timeout=per_sync_timeout)
        logging.info('found result[:500]: ' + repr(result)[:500])
        if result:
            result_items.append(result)

    if preserve_result_ordering:
        result_items = [work_item for index, work_item in result_items]

    return result_items


class ThreadedWorker(threading.Thread):
    """ Generic Threaded Worker
        Input to work_func: item from work_queue

    Example usage:

    import Queue

    urls_to_process = ["http://url1.com", "http://url2.com", "http://site1.com", "http://site2.com"]

    work_queue = Queue.Queue()
    result_queue = Queue.Queue()
    def process_url(url):
        # TODO: Do some work with the url
        return url

    def main():
        # spawn a pool of threads, and pass them queue instance
        for i in range(3):
            t = ThreadedWorker(work_queue, result_queue, work_func=process_url)
            t.setDaemon(True)
            t.start()

        # populate queue with data
        for url in urls_to_process:
            work_queue.put(url)

        # wait on the queue until everything has been processed
        work_queue.join()

        # print results
        print repr(result_queue)

    main()
    """

    def __init__(self, work_queue, result_queue, work_func, stop_when_work_queue_empty=True, queue_timeout=1):
        threading.Thread.__init__(self)
        self.work_queue = work_queue
        self.result_queue = result_queue
        self.work_func = work_func
        self.stop_when_work_queue_empty = stop_when_work_queue_empty
        self.queue_timeout = queue_timeout

    def should_continue_running(self):
        if self.stop_when_work_queue_empty:
            return not self.work_queue.empty()
        else:
            return True

    def run(self):
        while self.should_continue_running():
            try:
                # grabs item from work_queue
                work_item = self.work_queue.get(timeout=self.queue_timeout)

                # works on item
                work_result = self.work_func(work_item)

                # place work_result into result_queue
                self.result_queue.put(work_result, timeout=self.queue_timeout)
            except queue.Empty:
                logging.warning('ThreadedWorker Queue was empty or Queue.get() timed out')

            except queue.Full:
                logging.warning('ThreadedWorker Queue was full or Queue.put() timed out')

            except:
                logging.exception('Error in ThreadedWorker')

            finally:
                # signals to work_queue that item is done
                self.work_queue.task_done()


def start_logging_with_thread_info():
    try:
        formatter = logging.Formatter('[thread %(thread)-3s] %(message)s')
        print(logging.getLogger())
        logging.getLogger().handlers[0].setFormatter(formatter)
    except:
        logging.exception('Failed to start logging with thread info')


def stop_logging_with_thread_info():
    try:
        formatter = logging.Formatter('%(message)s')
        logging.getLogger().handlers[0].setFormatter(formatter)
    except:
        logging.exception('Failed to stop logging with thread info')