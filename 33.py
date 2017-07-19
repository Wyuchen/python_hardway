#!/usr/bin/python
#coding=utf-8
#笨办法学 Python-第三十三题
#while 循环的使用
i=0
numbers=[]
while i<6:
    print 'at the top i is %d' %i
    numbers.append(i)
    i+=1
    print 'numbers now: ',numbers
    print 'at the bottom i is %d' %i+'\n'

print 'the numbers:'
for num in numbers:
    print num
nums=[]

