#!/usr/bin/python
#coding=utf-8
#笨办法学 Python-第六题
#字符串的简单学习
#单个格式化字符串
x='there are %d type of pelple' % 10
binary='binary'
do_not="don't"
#多个格式化字符串
y="those who konw %s and those who %s" %(binary,do_not)
print  x
print  y
print "I said: %r" %x
print "I also said: %s" %y

#通过两个变量来组成字符串格式
sol= False
jok='is not that joke so funny ?! %r'
print jok % sol
#语句连接方式
w='i luckly num: '
e=str(10)
print w+e
#print  w % e


