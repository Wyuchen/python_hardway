#!/usr/bin/python
#coding=utf-8
#笨办法学 Python-第三十四题
#列表切片的使用和相应的取值
animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

print 'the animal at 1 is %s' %animals[1]
print 'the 3rd animal is %s' %animals[2]
print 'the 1st animal is %s' %animals[0]
print 'the animal at 3 is %s' %animals[3]
print 'the 5th animal is %s' %animals[4]
print 'the animal at 2 is %s' %animals[2]
print 'the 6th animal is %s' %animals[5]
print 'the animal at 4 is %s' %animals[4]

print '列表倒数第一个: %s' %animals[-1]

print '列表第二到第四个:%s' %animals[1:4]