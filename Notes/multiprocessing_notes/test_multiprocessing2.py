"""
lets try it 10 times now. Our computer doesn't have 10 cores, but its set up to where it can switch
off between cores when it isn't busy

"""

import multiprocessing
import time

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

if __name__ == "__main__":
    # create list so we can join all the processes
    processes = []

    for _ in range(10):
        p = multiprocessing.Process(target=do_something)
        p.start()
        processes.append(p)

    for process in processes:
        process.join()


    finish = time.perf_counter()

    print(f'Finished in {finish-start} second(s)')