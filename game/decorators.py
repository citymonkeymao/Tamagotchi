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
def death_check(func):
    def wrapper(*args, **kw):
        if args[0].dead:
            raise PetDeadException('playing with a dead animal', 1)
        else:
            func(*args,**kw)
    return wrapper
