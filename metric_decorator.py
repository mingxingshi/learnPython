# -*- coding: utf-8 -*-
import functools, time

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        f = fn(*args, **kw)
        end = time.time()
        print('%s executed in %s ms' % (fn.__name__,(end - start)*1000))
        return f
    return wrapper
    
#test
@metric
def fast(x, y):
    time.sleep(1)
    return x + y
    
@metric
def slow(x, y, z):
    time.sleep(3)
    return x * y * z
    
f = fast(11,22)
s = slow(11,22,33)
print(f, s)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试成功!')