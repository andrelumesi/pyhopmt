from concurrent.futures import ThreadPoolExecutor

def wait_on_future():
    f = executor.submit(pow, 5, 2)
    # This will never complete because there is only one worker thread and
    # it is executing this function.
    # print("depois")
    print(f.result())
 
executor = ThreadPoolExecutor(max_workers=1)
future = executor.submit(wait_on_future)
print("after future")
# while (not future.done):
#     print("waiting")
