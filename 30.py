#!/usr/bin/python
#coding=utf-8
#笨办法学 Python-第三十题
'''
方法一:
from sys import argv
script,people,cars,buses=argv #注意需要添加script
'''
#方法二
people=int(raw_input("please input the number of people:"))
cars=int(raw_input("please input the number of cars:"))
buses=int(raw_input("please input the numbers of buses:"))
if people < cars:
    print "people < cars"
elif people >cars:
    print 'people > cars'
else:
    print 'people = cars'

if buses >cars:
    print 'buses > cars'
elif buses < cars:
    print 'buses < cars'
else:
    print 'buses =cars'

