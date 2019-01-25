#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'测试访问限制'

__author__ = 'smx'

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
        
    def get_gender(self):
        return self.__gender
        
    def set_gender(self, gender):
        if gender not in ('male','female'):
            raise TypeError('bad gender')
        self.__gender = gender
        
#测试
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')