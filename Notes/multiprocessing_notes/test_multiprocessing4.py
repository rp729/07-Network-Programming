"""
unlike threading, arguments must be passed in with pickle
arguments have to be serialized, convert the python object to a format that can be deconstructed and reconstructed 


"""

import concurrent.futures
import time

start = time.perf_counter()

# now our function accepts a number of seconds
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return 'Done Sleeping...'

if __name__ == "__main__":

    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     # submit schedules a function to be executed and returns a future object
    #     # a future object encapsulates the execution of our function and allows us 
    #     # to check on it after its been scheduled, we can see if its running, done, or the result
    #     f1 = executor.submit(do_something, 1)
    #     f2 = executor.submit(do_something, 1)
    #     print(f1.result())
    #     print(f2.result())

    # using list comprehension
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(do_something, 1) for _ in range(10)]

        # pass in our list of futures objects results so it can be used with as_completed
        for f in concurrent.futures.as_completed(results):
            print(f.result())


    finish = time.perf_counter()

    print(f'Finished in {finish-start} second(s)')