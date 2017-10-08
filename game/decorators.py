import threading

def sync(func):
    '''decorator to keep thread safe'''
    threadLock = threading.Lock()
    def func_wrapper(*args, **kwargs):
        threadLock.acquire()
        ret = func(*args, **kwargs)
        threadLock.release()
        return ret
    return func_wrapper