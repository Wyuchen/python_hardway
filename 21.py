#!/usr/bin/python
#coding=utf-8
# 笨办法学 Python-第二十一题
#函数有返回值的
print "简单的四则运算:"
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

age=add(30,5)
height=subtract(78,4)
weight=multiply(90,2)
iq=divide(100,2)

print 'age:%d,height:%d,weight:%d,iq:%d'%(age,height,weight,iq)

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print "That becomes: ", what, "Can you do it by hand?"
