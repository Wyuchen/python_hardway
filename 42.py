#!/usr/bin/python
#coding=utf-8
#笨办法学 Python-第四十二题
#一个类中存在三个方法
class theThing(object):
    def __init__(self):
        self.number=0
    def some_function(self):
        print 'i got called'
    def add_me_up(self,more):
        self.number+=more
        print self.number
#实例化函数
a=theThing()
b=theThing()
#定义some_function()方法
a.some_function()
b.some_function()
#打印add_me_up()方法
print '原始number is %d' %a.number
print '调用add_me_up方法后number is '
a.add_me_up(20)
print '再次调用add_me_up方法后number is '
a.add_me_up(20)
print '调用之后number is %d' %a.number

print  '\n'

print '原始number is %d' % b.number
print '调用add_me_up方法后number is  '
b.add_me_up(30)
print '调用之后number is %d' %b.number
print '调用之后number is '
b.add_me_up(30)
