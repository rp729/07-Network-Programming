"""
Prove that these are actually coming in as they are completed,
    lets pass in a range of seconds

Start 5 second thread first, but since we use as_completed() method it prints
    the results in the order they are completed
"""
import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

# using a context manager
with concurrent.futures.ThreadPoolExecutor() as executor:

    seconds_list = [5, 4, 3, 2, 1]
    # list comprehension to create multiple threads
    results = [executor.submit(do_something, sec) for sec in seconds_list]

    # to get the results we can use another function, as_completed() from future object that 
    # gives us an iterator
    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()

print(f'Finished in {finish-start} second(s)')