# -*- coding: utf-8 -*-
import functools, time


def log(text=None):
    
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kw):
            if text != None:
                print('%s %s():' % (text, fn.__name__))
            print('begin call')
            start = time.time()
            print(fn(*args, **kw))
            end = time.time()
            print('end call')
            print('%s executed in %.f ms.\n' % (fn.__name__, (end - start)*1000))
        return wrapper
    return decorator
    

@log()
def f1(x, y):
    time.sleep(1)
    return x+y

@log('execute')
def f2(x, y, z):
    time.sleep(3)
    return x*y*z
    

f1(11,22)
f2(11,22,33)