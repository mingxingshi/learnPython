#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module' #表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释

__author__ = 'smx' #__author__变量把作者写进去

import sys  #导入sys模块

def test():
#sys模块有一个argv变量，用list存储了命令行的所有参数，argv至少有一个元素，因为第一个参数永远是该py文件的名称
    args = sys.argv 
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')
        
if __name__=='__main__':
    test()

#运行python3 hello.py获得的sys.argv就是['hello.py']；
#运行python3 hello.py smx获得的sys.argv就是['hello.py', 'smx']。

#注意最后两行代码
#当在命令行运行hello模块时，Python解释器会把特殊变量__name__置为__main__，此时if判断成立，将执行模块里的test()函数
#而如果在其他地方导入该hello模块时，if判断将失败，此时只会导入hello模块，而不会执行模块里面的test()函数，只有调用hello.test()时，才会执行
