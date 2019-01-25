# -*- coding: utf-8 -*-

name = input('Please input your name: ')
height = float(input('Please input your height(m): '))
weight = float(input('Please input your weight(kg): '))

def f_bmi(h, w):
    bmi = (w/h/h)
    if bmi<18.5:
        return(bmi,'过轻')
    elif bmi<25:
        return(bmi,'正常')
    elif bmi<28:
        return(bmi,'过重')
    elif bmi<32:
        return(bmi,'肥胖')
    else:
        return(bmi,'严重肥胖')

bmi = f_bmi(height,weight)
print('%s的bmi指数为%.1f，%s。' % (name,bmi[0],bmi[1]))
#print('%s的bmi指数为%.1f，%s。' % (name,f_bmi(height,weight)[0],f_bmi(height,weight)[1]))