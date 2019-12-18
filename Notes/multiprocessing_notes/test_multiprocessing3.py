"""
pass in an argument

unlike threading, arguments must be passed in with pickle
arguments have to be serialized, convert the python object to a format that can be deconstructed and reconstructed 


"""

import multiprocessing
import time

start = time.perf_counter()

# now our function accepts a number of seconds
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print('Done Sleeping...')

if __name__ == "__main__":
    # create list so we can join all the processes
    processes = []

    for _ in range(10):
        p = multiprocessing.Process(target=do_something, args=[1.5])
        p.start()
        processes.append(p)

    for process in processes:
        process.join()


    finish = time.perf_counter()

    print(f'Finished in {finish-start} second(s)')